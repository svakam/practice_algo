# Works consulted: Machine Learning: Linear Algebra, Coursera by Luis Serrano. 

import numpy as np

def augment(A, b):
    """
    Create an augmented matrix by horizontally stacking two matrices A and b. 
    E.g. in a system of linear equations, the coefficient feature matrix A and target vector b can be augmented to accomplish
    Gaussian elimination. 
    

    Returns:
    numpy.array representing [A | b]. 
    """

    return np.hstack((A, b))

def swap_rows(M, row_idx_1, row_idx_2):
    """
    Swap rows in the given matrix. 

    Parameters:
    - matrix (numpy.array): Input matrix to perform row swaps on
    - row_idx_1 (int): index of 1st row to be swapped
    - row_idx_2 (int): index of 2nd row to be swapped
    """

    # copy matrix M so changes don't affect original amtrix
    M = M.copy()
    # swap indexes
    M[[row_idx_1, row_idx_2]] = M[[row_idx_2, row_idx_1]]
    return M

def get_idx_first_non_zero_value_from_column(M, column, starting_row):
    """
    Retrieve index of the first non-zero value in a specified column of the matrix M.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values. 
    - column (int): The index of the column to search. 
    - starting_row (int): The starting row index for the search. 

    Returns: 
    int: The index of the first non-zero value in specified column starting from the 
    given row. Returns -1 if no non-zero value found. 
    """

    # Get the column array starting from the specified row
    column_array = M[starting_row:,column]
    
    # iterate over every value in column array
    for i, val in enumerate(column_array):
        if not np.isclose(val, 0, atol=1e-5):
            # if non-zero value found, add starting row's value to i to get correct 
            # index of non-zero value within column  
                index = i + starting_row
                return index
        
    # if no non-zero value found below this pivot, return -1
    return -1

def get_idx_first_non_zero_value_from_row(M, row, augmented = False):
    """
    Find index of first non-zero value in specified row of the given matrix. If 
    augmented matrix, ignore the last column (constants).  

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values. 
    - row (int): The index of the row to search. 
    - augmented (bool): True if input is an augmented matrix. 

    Returns:
    int: The index of the first non-zero value in the specified row. Returns -1 
    if no non-zero value found. 
    """

    M = M.copy()

    if augmented == True:
        M = M[:, :-1] # get all rows, get all columns except last

        row_array = M[row]
        for i, val in enumerate(row_array):
            if not np.isclose(val, 0, atol=1e-5):
                return i
    
    return -1

def row_echelon_form(M):
    """
    Accepts an augmented matrix and returns its row-echelon form.
    
    Parameters:
    - M (numpy.array): Augmented matrix. 

    Returns:
    - numpy.array: input matrix in row-echelon form.
    """

    num_rows = len(M)

    for row in range(num_rows):
        pivot_candidate = M[row, row]

        # if pivot zero, look for a row at this column idx to swap with whose value at this idx is non-zero
        if np.isclose(pivot_candidate, 0) == True:
            
            # get index to swap with and swap rows
            idx_first_non_zero_value_below_pivot_candidate = \
                get_idx_first_non_zero_value_from_column(M, row, row)
            M = swap_rows(M, row, idx_first_non_zero_value_below_pivot_candidate)

            # now can set pivot to newly swapped row at this index
            pivot = M[row, row]

        # if pivot already non-zero, it is the pivot for this row 
        else:
            pivot = pivot_candidate
        
        # divide current row by pivot, so new pivot will be 1
        M[row] = 1/pivot * M[row]

        # perform row reduction for rows below current row
        for j in range(row + 1, num_rows):
            
            # get value below pivot and reduce the row
            value_below_pivot = M[j, row]
            # set this row 
            M[j] = M[j]

def back_substitution(M):
    return None

def gaussian_elimination(A, b):
    """
    1) Augment coefficient and target matrices,
    2) Transform matrix into row-echelon form,
    3) Back-substitute rows. 
    """

    augmented_M = augment(A, b)

    row_echelon_M = row_echelon_form(augmented_M)

    reduced_row_echelon_M = back_substitution(row_echelon_M)

    return reduced_row_echelon_M

def main():
    """
    A = coefficient matrix, n rows = n cols (square matrix). 
    b = target vector, length n. 
    """
    # set up inputs
    A = np.array([[0,2,1],[1,1,1],[1,2,1]])
    b = np.array([[3],[6],[12]])

    # if determinant of coefficient matrix is 0, don't try Gaussian elimination
    det_A = np.linalg.det(A)
    if np.isclose(det_A, 0) == True:
        return 'Singular system'

    # avoid modifying originals
    A = A.copy()
    b = b.copy()

    # convert matrices to float to prevent integer division

    solution = gaussian_elimination(A, b)

if __name__ == "__main__":
    main()
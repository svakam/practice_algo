import numpy as np

def print_singular(run):
    if run: 
        print("Singular")
    else:
        print("Not Singular")

def is_singular(matr):
    """
    Calculates whether the input matrix is singular and returns a boolean. 
    """

    det = 0.0

    num_rows = matr.length, num_cols = matr[0].length
    
    # fwd loop
    start_col = 0
    diag_prod = 1.0

    while start_col < num_cols:
        curr_col = start_col
        
        for curr_row in range(num_rows):
            
            if curr_col == num_cols:
                curr_col = 0
            
            diag_prod *= matr[curr_row][curr_col]
            
            curr_col += 1    

        start_col += 1

        det += diag_prod


    # bkwd loop
    start_col = num_cols - 1
    diag_prod = 1.0

    while start_col >= 0:
        curr_col = start_col
        
        for curr_row in range(num_rows):
            
            if curr_col == 0:
                curr_col = num_cols - 1
            
            diag_prod *= matr[curr_row][curr_col]
            
            curr_col -= 1

        start_col += 1

        det -= diag_prod


    return det == 0.0

def main():
    arrNS_1 = [[1,1],[1,2]];
    arrS_1 = [[1,1],[2,2]];
    arrNS_2 = [[1,1,1],[1,2,1],[1,1,2]];

    print_singular(f"{is_singular(arrNS_1)}, expected False")
    print_singular(f"{is_singular(arrS_1)}, expected True")
    print_singular(f"{is_singular(arrNS_2)}, expected False")


if __name__ == "__main__":
    main()
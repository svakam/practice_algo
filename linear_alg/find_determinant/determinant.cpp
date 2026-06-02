#include <iostream>
#include <string>
#include <stdexcept>

std::string print_singular(bool isSingularResult) {
    return isSingularResult ? "Singular" : "Not Singular";
} 

bool is_singular(float matr[][2], int num_rows, int num_cols) {
    /*
        Calculates whether a matrix is singular (squares only).
        Inputs: matr[]: Input matrix
        Output: Whether the matrix is singular (True) or not (False). 
    */

    // input checks
    if (matr == nullptr) {
        throw std::invalid_argument("Null input for matrix.");
    }
    if (num_rows < 2) {
        return false;
    }
    if (num_cols == 2 && num_rows == 2) { // if 2 rows, return ad - bc
        return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0];
    }


    /*
       diag_prod: accumulator for just 1 diagonal (product) 
       det: accumulator tracking total summation of matrix elements
       col_start: tracker for start of diagonal; starts at 0 and increments until out of bounds (i.e. equals num cols)
    */
    float det = 0.0f;

    // fwd loop: repeats as long as more diagonals to add
    int col_start = 0;
    
    while (col_start < num_cols) {
        float diag_prod = 1.0f;

        for (int curr_row = 0, curr_col = col_start; curr_row < num_rows; curr_row++) {

            // "typewriter": if still more rows to go but at end of column, reset column to 0
            if (curr_col == num_cols) {
                curr_col = 0;
            }

            // multiply current product of the diagonal with this element
            diag_prod *= matr[curr_row][curr_col];

            curr_col++;
        }
        
        det += diag_prod;

        col_start++;
    }

    // bkwd loop: repeats as long as more diagonals to subtract
    col_start = num_cols - 1;
    
    while (col_start >= 0) {
        float diag_prod = 1.0f;

        for (int curr_row = 0, curr_col = col_start; curr_row < num_rows; curr_row++) { // start from 0th row again but rightmost column

            if (curr_col < 0) {
                curr_col = num_cols - 1;
            }

            diag_prod *= matr[curr_row][curr_col];

            curr_col--;
        }

        det -= diag_prod;
        
        col_start--;
    }

    return det == 0.0;
}

int main() {
    float arrNS_1[2][2] = {{1,1},{1,2}};
    float arrS_1[2][2] = {{1,1},{2,2}};
    float arrNS_2[3][3] = {{1,1,1},{1,2,1},{1,1,2}};
    // float arr_3[3][3] = {{1,0,1},{0,1,0},{3,3,3}}};
    // float arr_4[3][3] = {{1,1,1},{1,1,2},{0,0,-1}};
    // float arr_5[3][3] = {{1,1,1},{0,0,2},{0,0,3}};
    // float arr_6[3][3] = {{1,2,5},{0,3,-2},{2,4,10}};

    std::cout << print_singular(is_singular(arrNS_1, 2, 2)) << ", expected False" << std::endl;
    std::cout << print_singular(is_singular(arrS_1, 2, 2)) << ", expected True" << std::endl;
    std::cout << print_singular(is_singular(arrS_1, 3, 3)) << ", expected False" << std::endl;


}

/*
init. bool variable dir to hold direction of diag (if true, fwd; else bkwd)
init. accumulator var acc to hold calculated determinant value
init. arr access indices i, j; i tracks rows, j tracks cols
(rule: if dir == fwd, then adding to acc, else subtracting)
    - how do we know we've reached end of diagonal? 

if matr is 2x2, just return arr[0,0] * arr[1,1] - arr[0,1] * arr[1,0]

a diagonal is completed (i.e. stop multiplying elements) when # rows finished
if # cols finished, reset col tracker to 0

a direction is completed (i.e. switch to subtracting products) when # start_col reaches num_cols

*/


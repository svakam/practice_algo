#include <iostream>
#include <string>
#include <stdexcept>


void add_to_acc(float& matr[], int& i, int& j, float& acc, bool& fwd) {
    fwd ? acc += matr[i][j] : acc -= matr[i][j];
}

bool is_singular(float* matr[]) {
    /*
        Calculates whether a matrix is singular (squares only).
        Inputs: matr[]: Input matrix
        Output: Whether the matrix is singular (True) or not (False). 
    */

    int row_length = matr[0].length(), col_length = matr.length;

    if (matr == null) {
        throw std::invalid_argument("Null input for matrix.");
    }

    // if 1 row, return False
    if (col_length < 2) {
        return false;
    }

    // if 2 rows, return ad - bc
    if (col_length == 2 && row_length == 2) {
        return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0];
    }


    // acc: accumulator tracking total summation of matrix elements
    // j_start: diagonal tracker; starts at 0 and increments until out of bounds
    // fwd: boolean tracking whether diagonal indices go forward (j++) or backward (j--)
    int acc = 0, col_start = 0;
    bool fwd = true;

    // fwd loop
    while (col_start <= row_length) {
        for (int curr_col = col_start; j <= i; j++) {
            // "typewriter": if still more rows to go but at end of column, reset column to 0
            if (curr_i )
            add_to_acc(matr, i, j, acc, fwd);
        }
        
        curr_j++;
    }

    // bkwd loop
    fwd = false;
    j_start = max_diag;
    while (curr_j > 0) {
        
    }

}

int main() {
    int arrNS_1[] = {[1,1],[1,2]};
    int arrS_1[] = {[1,1],[2,2]};
    int arrNS_2[] = {[1,1,1],[1,2,1],[1,1,2]};
    // int arr_3[] = {[1,0,1],[0,1,0],[3,3,3]};
    // int arr_4[] = {[1,1,1],[1,1,2],[0,0,-1]};
    // int arr_5[] = {[1,1,1],[0,0,2],[0,0,3]};
    // int arr_6[] = {[1,2,5],[0,3,-2],[2,4,10]};

    std::cout << print_singular(is_singular(arrNS_1));
    std::cout << print_singular(is_singular(arrS_1));

}

/*
init. bool variable dir to hold direction of diag (if true, fwd; else bkwd)
init. accumulator var acc to hold calculated determinant value
init. arr access indices i, j; i tracks rows, j tracks cols
    - how do we know we're out of diagonals in fwd dir? looking at cols, 
    a diagonal start array indx j_start; if j_start OOB, start diagonals bkwd
(rule: if dir == fwd, then adding to acc, else subtracting)
    - how do we know we've reached end of diagonal? 

if matr is 2x2, just return arr[0,0] * arr[1,1] - arr[0,1] * arr[1,0]
else:




*/


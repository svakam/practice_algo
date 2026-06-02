#include <random>
#include <vector>
#include <stdexcept>
#include <iostream>

std::vector<float> create_y_vals(int size, float lower, float upper) {
    std::vector<float> arr(size);

    // random-generate floats for y values and place into array
    std::random_device rd; // seed
    std::mt19937 gen(rd()); // Mersenne Twister RNG
    std::uniform_real_distribution<float> dist(lower, upper);
    for (int i = 0; i < size; i++) {
        arr[i] = dist(gen);
    }

    return arr;
}

bool not_in_middle(int i, int window_size) {
    float half_window = window_size / 2;
    float mid_window = ((i + half_window) + (i - half_window)) / 2;

    return abs(i - mid_window) > 0.5; // accounts for even-sized windows
}

std::vector<float> moving_avg(std::vector<float> arr, int arr_size, int window_size) {
    /*
        Takes an array of values and averages them over the window_size.
    */

    std::vector<float> moving_avg_vals(arr_size);

    for (int i = 0; i < arr_size; i++) {
        /* 
            handle edge cases where curr idx is not in the middle of where window is
            (e.g. if window size 5, i = 1 or 2 (beginning of arr) or i = 99 or 100 (end))
        */ 
        if (i == 0 || i == arr_size - 1) { // at very beginning or very end, just set val to array val
            moving_avg_vals[i] = arr[i];
        } else {
            // if somewhere within window but not in middle, set window upper bound to double that of i - lower bound
            if (not_in_middle(i, window_size)) {
                if ((i - window_size) - i)
            }
        }
        
    }
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: ./moving_avg <lower_bound_float> <upper_bound_float>" << std::endl;
        return 1;
    }

    float lower = std::stof(argv[1]), upper = std::stof(argv[2]); // bounds of possible y values
    int window_size = std::stoi(argv[3]);

    if (lower >= upper || abs(lower - upper) > 50.0) {
        std::cerr << "Bad lower and upper bound args; upper - lower > 50.0" << std::endl;
        return 1;
    }

    if (window_size < 1) {
        std::cerr << "Bad window size; window size must be > 1 units" << std::endl;
        return 1;
    }

    int size = 50; // array size

    int x[size] = {};
    for (int i = 0; i < size; i++) {
        x[i] = i + 1;
    }

    std::vector<float> y_vals = create_y_vals(size, lower, upper);

    std::vector<float> moving_avg_vals = moving_avg(y_vals, size, window_size);

    

    return 0;
}
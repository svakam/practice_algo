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

std::vector<float> moving_avg(std::vector<float> arr) {

}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: ./moving_avg <lower_bound_float> <upper_bound_float>" << std::endl;
        return 1;
    }

    float lower = std::stof(argv[1]), upper = std::stof(argv[2]); // bounds of possible y values

    if (lower >= upper || abs(lower - upper) > 50.0) {
        std::cerr << "Bad lower and upper bound args; upper - lower > 50.0" << std::endl;
        return 1;
    }

    int size = 50; // array size

    int x[size] = {};
    for (int i = 0; i < size; i++) {
        x[i] = i + 1;
    }

    std::vector<float> y_vals = create_y_vals(size, lower, upper);

    std::vector<float> moving_avg_vals = moving_avg(y_vals);

    

    return 0;
}
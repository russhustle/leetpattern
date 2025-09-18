#ifndef PRINT_UTILS_HPP
#define PRINT_UTILS_HPP

#include <iostream>
#include <vector>

template <typename T>
void printVector(const std::vector<T>& vec) {
    std::cout << "[";
    for (size_t i = 0; i < vec.size(); i++) {
        std::cout << vec[i];
        if (i < vec.size() - 1) std::cout << ", ";
    }
    std::cout << "]" << std::endl;
}

template <typename T>
void print2DVector(const std::vector<std::vector<T>>& vec) {
    std::cout << "[" << std::endl;
    for (const auto& row : vec) {
        std::cout << "  ";
        printVector(row);
    }
    std::cout << "]" << std::endl;
}

#endif
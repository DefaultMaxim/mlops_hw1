#include "VectorStandardization.h"

#include <cmath> // Для sqrt
#include <stdexcept> // Для обработки ошибок

// Рассчитать среднее значение
double VectorStandardization::calculateMean(const std::vector<double>& inputVector) {
    if (inputVector.empty()) {
        throw std::invalid_argument("Vector is empty. Cannot calculate mean.");
    }
    double sum = 0.0;
    for (double value : inputVector) {
        sum += value;
    }
    return sum / inputVector.size();
}

// Рассчитать стандартное отклонение
double VectorStandardization::calculateStdDev(const std::vector<double>& inputVector, double mean) {
    if (inputVector.size() < 2) {
        throw std::invalid_argument("Vector must contain at least two elements to calculate standard deviation.");
    }
    double sumSquares = 0.0;
    for (double value : inputVector) {
        sumSquares += (value - mean) * (value - mean);
    }
    return std::sqrt(sumSquares / (inputVector.size() - 1));
}

// Стандартизация вектора
std::vector<double> VectorStandardization::standardize(const std::vector<double>& inputVector) {
    if (inputVector.empty()) {
        throw std::invalid_argument("Vector is empty. Cannot standardize.");
    }

    double mean = calculateMean(inputVector);
    double stdDev = calculateStdDev(inputVector, mean);

    if (stdDev == 0) {
        throw std::invalid_argument("Standard deviation is zero. Cannot standardize.");
    }

    std::vector<double> standardizedVector;
    standardizedVector.reserve(inputVector.size());

    for (double value : inputVector) {
        standardizedVector.push_back((value - mean) / stdDev);
    }

    return standardizedVector;
}

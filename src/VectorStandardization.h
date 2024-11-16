#ifndef VECTOR_STANDARDIZATION_H
#define VECTOR_STANDARDIZATION_H

#include <vector>

class VectorStandardization {
public:
    // Стандартизировать вектор
    static std::vector<double> standardize(const std::vector<double>& inputVector);

private:
    // Рассчитать среднее значение вектора
    static double calculateMean(const std::vector<double>& inputVector);

    // Рассчитать стандартное отклонение вектора
    static double calculateStdDev(const std::vector<double>& inputVector, double mean);
};

#endif // VECTOR_STANDARDIZATION_H

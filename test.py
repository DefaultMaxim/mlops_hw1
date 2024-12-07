import numpy as np
import _vector_standardization

def test_vector_standardization():
    # Пример входного вектора
    input_vector = [1.0, 2.0, 3.0, 4.0, 5.0]

    # Результат стандартизации C++
    result = _vector_standardization.standardize(input_vector)

    # Результат стандартизации с помощью numpy
    np_array = np.array(input_vector)
    np_mean = np.mean(np_array)

    np_std = np.std(np_array, ddof=1)  
    expected = (np_array - np_mean) / np_std

    # Проверяем, что каждый элемент примерно равен
    print(f'Numpy реализация: {expected}')
    print(f'С++ реализация: {np.round(result, 10)}')
    assert np.allclose(result, expected, rtol=1e-7), f"Результат {result} не соответствует ожиданию {expected}"

    print("Тест пройден! Реализация соответствует numpy.")

if __name__ == "__main__":
    test_vector_standardization()

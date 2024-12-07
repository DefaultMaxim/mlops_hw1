# Используем официальный python-образ в качестве базы
FROM python:3.9-slim

# Устанавливаем инструменты для сборки C++
RUN apt-get update && apt-get install -y g++ cmake && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости для сборки Python пакета
# build для сборки wheel, pybind11 для биндингов
RUN pip install --upgrade pip setuptools wheel build pybind11

# Устанавливаем numpy для тестов (эталонная библиотека)
RUN pip install numpy

# Определим рабочую директорию
WORKDIR /app

# Копируем все необходимые файлы проекта
COPY pyproject.toml setup.py MANIFEST.in ./
COPY src/ src/
COPY test.py .

# Шаг 4: Выполняем сборку пакета внутри Docker
RUN python3 -m build

# Устанавливаем собранный пакет из дистрибутива
RUN pip install dist/vector_standardization-0.1-*.whl

# Шаг 5: Запускаем тесты внутри контейнера
# При запуске контейнера по умолчанию запустим тесты
CMD ["python3", "test.py"]

import os
import sys
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
import pybind11

# Определим расширение
class get_pybind_include(object):
    """Возвращает путь к заголовочному файлу pybind11 для использования в расширении."""

    def __str__(self):
        # Используем pybind11 для поиска нужных заголовочных файлов
        return pybind11.get_include()

class build_ext_subclass(build_ext):
    """Подкласс для поддержки использования CMake или других инструментов сборки."""
    def build_extensions(self):
        # Если необходимо использовать CMake для сборки, добавьте эту логику
        build_ext.build_extensions(self)

# Определяем расширение с использованием pybind11
ext_modules = [
    Extension(
        "vector_standardization",  # Имя расширения (модуля)
        sources=["src/VectorStandardization.cpp", "src/bindings.cpp"],  # Путь к исходникам
        include_dirs=[get_pybind_include()],  # Путь к pybind11
        language="c++",  # Язык C++
        extra_compile_args=["-O3", "-Wall", "-std=c++17", "-fPIC"],  # Флаги компилятора
        extra_link_args=["-undefined", "dynamic_lookup"],  # Линковка с динамическим поиском
    ),
]


# Настроим setuptools для использования кастомного build_ext
setup(
    name="vector_standardization",
    version="0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="Vector Standardization with pybind11",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext_subclass},  # Подкласс для build_ext
    zip_safe=False,
    packages=["vector_standardization"],  # Указываем пакеты, если они есть
    install_requires=["pybind11"],  # Зависимости
)

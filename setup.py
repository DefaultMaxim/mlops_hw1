from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

class get_pybind_include(object):
    def __str__(self):
        import pybind11
        return pybind11.get_include()

class build_ext_subclass(build_ext):
    def build_extensions(self):
        build_ext.build_extensions(self)

ext_modules = [
    Extension(
        "_vector_standardization",
        sources=["src/VectorStandardization.cpp", "src/bindings.cpp"],
        include_dirs=[get_pybind_include(), 'src'],
        language="c++",
        extra_compile_args=["-O3", "-Wall", "-std=c++17", "-fPIC"],
        # extra_link_args=["-undefined", "dynamic_lookup"],
    ),
]



setup(
    name="vector_standardization",
    version="0.1",
    # Не указывайте packages и не создавайте пакет с таким же именем
    # packages=["vector_standardization"], <- убираем
    ext_modules=ext_modules,
    setup_requires=["pybind11>=2.6.0"],
    install_requires=["pybind11"],
    zip_safe=False,
)

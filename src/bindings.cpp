#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "VectorStandardization.h"

namespace py = pybind11;

PYBIND11_MODULE(vector_standardization, m) {
    m.doc() = "Python bindings for vector standardization";

    m.def("standardize", &VectorStandardization::standardize,
          "Standardize a vector (mean 0, stddev 1)",
          py::arg("input_vector"));
}

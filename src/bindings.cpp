#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "VectorStandardization.h"

namespace py = pybind11;

PYBIND11_MODULE(_vector_standardization, m) {
    m.doc() = "Module provides vector standardization functionality";
    m.def("standardize", &VectorStandardization::standardize,
          py::arg("input_vector"),
          "Standardize a given vector of doubles");
}



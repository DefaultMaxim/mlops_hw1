PYTHON_VERSION := 3.12
PYTHON_INCLUDE := $(shell python3-config --includes)
PYTHON_LIBS := $(shell python3-config --ldflags)
PYBIND11_INCLUDE := $(shell python3 -m pybind11 --includes)

CXX := clang++
CXXFLAGS := -O3 -Wall -shared -std=c++17 -fPIC $(PYTHON_INCLUDE) $(PYBIND11_INCLUDE)
LDFLAGS := $(PYTHON_LIBS) -undefined dynamic_lookup

TARGET := vector_standardization$(shell python3-config --extension-suffix)

all: $(TARGET)

$(TARGET): bindings.cpp VectorStandardization.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)

clean:
	rm -f $(TARGET)

# Set up swig
find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})
include_directories(/usr/lib64/python3.6/site-packages/numpy/core/include)

option(BUILD_PYTHON "Build Python SWIG module" ON)
if(BUILD_PYTHON)
    add_subdirectory(python)
endif()

option(BUILD_R "Build R SWIG module" OFF)
if(BUILD_R)
    add_subdirectory(R)
endif()

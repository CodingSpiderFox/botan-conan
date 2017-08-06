cmake_minimum_required(VERSION 3.1.2)
project(PackageTest
  LANGUAGES CXX
  VERSION 2.1.0
  )

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(CMAKE_CXX_STANDARD 11)

add_executable(package_test
  package_test.cpp
  )

target_link_libraries(package_test
  CONAN_PKG::Botan
  )

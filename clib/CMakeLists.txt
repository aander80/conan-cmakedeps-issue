cmake_minimum_required(VERSION 3.15)
project(clib)

find_package(header_generator)

set(CLASSES_H ${CMAKE_BINARY_DIR}/classes.h)

generate_header(
    CLASSES A B C
    OUTPUT_FILE ${CLASSES_H}
)

add_custom_target(classes_h ALL
    DEPENDS ${CLASSES_H}
)

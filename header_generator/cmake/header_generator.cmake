cmake_minimum_required(VERSION 3.25)

function(generate_header)

    set(OPTIONS "")
    set(ONE_VALUE_ARGS
        OUTPUT_FILE
    )
    set(MULTI_VALUE_ARGS
        CLASSES
        DEPENDS
    )
    cmake_parse_arguments(ARG "${OPTIONS}" "${ONE_VALUE_ARGS}" "${MULTI_VALUE_ARGS}" ${ARGN})

    add_custom_command(
        COMMAND python -m header_generator ${ARG_CLASSES} -o ${ARG_OUTPUT_FILE}
        DEPENDS ${ARG_DEPENDS}
        OUTPUT ${ARG_OUTPUT_FILE}
    )

endfunction()

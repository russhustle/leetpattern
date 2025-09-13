cmake_minimum_required(VERSION 3.10)
project(CppProblems)
# set compiler to g++
set(CMAKE_CXX_COMPILER "/home/linuxbrew/.linuxbrew/bin/g++-15")
set(CMAKE_C_COMPILER "/home/linuxbrew/.linuxbrew/bin/gcc-15")
# Set C++ standard
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add compiler flags for better debugging and warnings
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -g -std=c++23")

# Function to recursively find all .cc files
file(GLOB_RECURSE CPP_FILES "*.cc")

# Create executables for each .cc file
foreach(CPP_FILE ${CPP_FILES})
    # Get filename without extension
    get_filename_component(EXEC_NAME ${CPP_FILE} NAME_WE)
    
    # Get the directory of the file to create unique names if needed
    get_filename_component(FILE_DIR ${CPP_FILE} DIRECTORY)
    get_filename_component(DIR_NAME ${FILE_DIR} NAME)
    
    # Create unique executable name (useful if you have same filenames in different folders)
    if(NOT "${DIR_NAME}" STREQUAL "")
        set(UNIQUE_EXEC_NAME "${DIR_NAME}_${EXEC_NAME}")
    else()
        set(UNIQUE_EXEC_NAME "${EXEC_NAME}")
    endif()
    
    # Create executable
    add_executable(${UNIQUE_EXEC_NAME} ${CPP_FILE})
    
    # Add to a list for batch operations
    list(APPEND ALL_EXECUTABLES ${UNIQUE_EXEC_NAME})
endforeach()

# Create a custom target to build all executables
add_custom_target(build_all 
    DEPENDS ${ALL_EXECUTABLES}
    COMMENT "Building all C++ problems"
)

# Create a custom target to run all executables
add_custom_target(test_all
    COMMENT "Running all C++ problems"
)

# Add run commands for each executable
foreach(EXEC ${ALL_EXECUTABLES})
    add_custom_command(TARGET test_all POST_BUILD
        COMMAND echo "Running ${EXEC}..."
        COMMAND ./${EXEC} || echo "❌ ${EXEC} failed"
        COMMAND echo "✅ ${EXEC} passed"
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
        COMMENT "Running ${EXEC}"
    )
endforeach()
cmake_minimum_required(VERSION 3.8)
project(bot_pkg1)

# Compiler options for GCC or Clang
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(xacro REQUIRED)
find_package(ros_gz_bridge REQUIRED)
find_package(ros_gz_sim REQUIRED)

# Add directories to install
install(
  DIRECTORY meshes urdf launch
  DESTINATION share/${PROJECT_NAME}
)

# Install executable or library if needed
# For example, if you have any nodes to install
# install(TARGETS your_target
#   DESTINATION lib/${PROJECT_NAME}
# )

# Test dependencies (optional)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

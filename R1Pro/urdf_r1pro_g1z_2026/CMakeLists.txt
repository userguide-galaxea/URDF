cmake_minimum_required(VERSION 3.8)
project(r1pro_urdf)

# 依赖查找
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

# 资源安装
install(DIRECTORY config launch meshes urdf
    DESTINATION share/${PROJECT_NAME}
)

# 依赖导出
ament_export_dependencies(rclcpp std_msgs)
ament_package()
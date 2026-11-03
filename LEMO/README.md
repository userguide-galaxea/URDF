# LEMO robot description

ROS 1 catkin description package for the LEMO dual-A1Z platform with G1Z grippers.
The ROS package name is `lemo_description`.

## Display

Place this package in a catkin workspace, build the workspace and source its
`devel/setup.bash`, then run:

```bash
roslaunch lemo_description display.launch
```

Use `gui:=false` to publish default joint states without joint sliders.

## Model

- `urdf/LEMO.urdf`: 19 links and 18 joints, including six revolute joints per arm
  and two prismatic finger joints per gripper. Each right finger mimics its
  corresponding left finger with multiplier -1.
- `meshes/`: all visual and collision meshes referenced by the URDF.
- `config/LEMO.rviz`: RViz configuration with fixed frame `base_link`.
- `config/base_mass_properties.json`: base CAD mass properties and mesh
  registration provenance; this file is not loaded at runtime.

Lengths are in metres, masses in kilograms and inertias in kg m². The base STL
uses scale `0.001 0.001 0.001`; arm meshes use unit scale. Arm mounts are at
`(0, ±0.375, 0.005)` m, both with zero rotation.

Base mesh registration is estimated from mesh geometry and uniform-density
mass properties and has not been confirmed against the CAD frame. Gripper
limits of 3 N and 10.47 m/s are inherited values, not validated hardware limits.
The historical `rIght` spelling in finger names is retained for compatibility.

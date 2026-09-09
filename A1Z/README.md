# A1Z models

- `A1Z_Flange`: six-axis arm ending at the bare flange.
- `A1Z_G1Z`: the same arm with the G1Z gripper body and two moving fingers.

The two models have identical `base_link` through `arm_link5` definitions and
meshes, and identical `arm_joint1` through `arm_joint6` definitions. Mesh package
prefixes differ. `arm_link6` deliberately differs: the G1Z model includes the
stationary gripper body in this link, while the Flange model contains only the
bare flange. Removing just the two finger links does not produce the Flange model.

The G1Z update preserves the supplied masses, centers of mass, inertia tensors,
meshes and gripper kinematics. The six arm joints retain the repository's existing
effort and velocity limits instead of the CAD export's zero values. Existing
link, joint and mesh names (including the historical `rIght` spelling) are retained
for compatibility; mesh filenames match the URDF references exactly on Linux.

The left finger travels from 0 to 0.048 m along its local Y axis. The right finger
travels from -0.048 to 0 m and mimics the left with multiplier -1 and offset 0.
Both fingers use `effort="3"` and `velocity="10.47"`; the velocity has the same
numeric value as J5/J6. Because the finger joints are prismatic, URDF interprets
these values as 3 N and 10.47 m/s, whereas J5/J6 velocity is in rad/s. These values
are not a transmission conversion of a 3 Nm motor rating. Motor torque and speed
require transmission geometry/ratio to derive physical linear force and speed;
the configured values have not been validated as hardware operating limits.

Offline checks passed for XML structure, the connected link/joint trees, joint
axes and ranges, mimic consistency, case-sensitive mesh references, binary STL
sizes and finite coordinates, and all inertia tensors (positive principal moments
and rigid-body triangle inequalities). The G1Z model has 9 links and 8 joints;
the Flange model has 7 links and 6 joints.

The existing CSV and export logs are historical CAD artifacts, not the current
model specification. These remain ROS 1 catkin packages. Package names and launch
URDF paths have been aligned, and display launch files no longer reference a
missing RViz configuration. No ROS/RViz/Gazebo runtime, catkin build, hardware test,
or independent CAD mass-property verification was performed.

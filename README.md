# SFG Livox ROS Driver 2

This is a specialized fork of the official [Livox ROS Driver 2](https://github.com/livox-SDK/livox_ros_driver2). Please refer to the upstream repository for comprehensive hardware configuration instructions, JSON parameter details, and supported LiDAR models.

## Why This Exists?

The official driver relies on custom shell scripts for building and defaults to a reliable QoS profile for its publishers. This fork was created to address two specific architectural needs:

1. **Native ROS 2 Tooling:** Removing the proprietary `build.sh` wrapper allows the package to build natively alongside other packages in standard ROS 2 workspaces using `colcon`.
2. **Network Stability on Mobile Platforms:** Publishing high-bandwidth LiDAR point clouds with a reliable QoS can severely saturate Wi-Fi networks and cause massive latency spikes, particularly on hardware like the Create3 running Fast DDS. This fork switches publishers to `BEST_EFFORT` reliability to prevent network saturation.

## Changelog & Modifications

* **`colcon` Compatibility:** Removed upstream build scripts; the package is now fully compatible with a standard `colcon build`.
* **QoS Optimization:** Switched point cloud publishers to `BEST_EFFORT`.
* **Modern Distribution Support:** Added support for ROS 2 kilted.
* **`tf2` Tree Flexibility:** Separated `frame_id` parameters for IMU and point cloud data.
* **Package Cleanup:** Fixed variable expansion and removed deprecated group syntax in `package.xml`.

## Usage Differences from Upstream

Because the build system and default launch files were modified, compiling and running this fork differs from the official documentation.

### Building

Clone this repository into your workspace's `src` directory and build directly with `colcon`:

```bash
export COLCON_WS=...

cd ${COLCON_WS}/src
git clone https://github.com/sfg-autonomous-systems/sfg_livox_ros_driver2 livox_ros_driver2
cd ..
colcon build --packages-select livox_ros_driver2 --symlink-install
```
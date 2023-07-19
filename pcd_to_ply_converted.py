import open3d as o3d
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pcd_to_ply_converted.py <file_name>")
        sys.exit(1)

    file_name = sys.argv[1]
    pcd = o3d.io.read_point_cloud(file_name)
    pcd.estimate_normals()

    target_file = file_name[:-4]+".ply"
    o3d.io.write_point_cloud(target_file, pcd)
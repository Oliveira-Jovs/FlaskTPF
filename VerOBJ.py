import open3d as o3d

# Carrega e visualiza o arquivo .obj
mesh = o3d.io.read_triangle_mesh("scene_mesh_textured.obj")
o3d.visualization.draw_geometries([mesh])

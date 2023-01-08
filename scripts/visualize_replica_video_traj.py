import sys

import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.animation as animation
from scipy.spatial.transform import Rotation
from coord import Coord

from dataloader import read_files_replica

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

def update(i, coords, ax):
    if i > 0:
        ax.lines.clear()
    coords[i].draw_coord(ax)

print("start.")

# load dataset
_, camera_params, _ = \
    read_files_replica(folder_path="data/Replica/", data_name="office0_original", delta=1)
scale = 1
camera_params[:, 3:6] *= scale
N = len(camera_params)

# set data
coords = []
for param in camera_params:
    rot = Rotation.from_rotvec(param[0:3])
    R = rot.as_matrix()
    t = param[3:6]

    coord = Coord(0.1, 1.0)
    coord.transform(R, t)
    coords.append(coord)

# set range
max_range = np.array([camera_params[:, 3].max()-camera_params[:, 3].min(),
                        camera_params[:, 4].max()-camera_params[:, 4].min(),
                        camera_params[:, 5].max()-camera_params[:, 5].min()]
                    ).max()
mid_x = (camera_params[:, 3].max() + camera_params[:, 3].min()) * 0.5
mid_y = (camera_params[:, 4].max() + camera_params[:, 4].min()) * 0.5
mid_z = (camera_params[:, 5].max() + camera_params[:, 5].min()) * 0.5
ax.set_xlim(mid_x - max_range*0.5, mid_x + max_range*0.5)
ax.set_ylim(mid_y - max_range*0.5, mid_y + max_range*0.5)
ax.set_zlim(mid_z - max_range*0.5, mid_z + max_range*0.5)

# set label
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# set view angle
ax.view_init(elev=30, azim=260)

fps = 30.0
ani = animation.FuncAnimation(fig, update, N, fargs=(coords, ax), interval=1.0/fps*1000)

ani.save("outputs/replica_traj.gif", writer="pillow")

print(f"start point: {camera_params[0, 3:6]}")
print(f"end point: {camera_params[-1, 3:6]}")

print("end.")

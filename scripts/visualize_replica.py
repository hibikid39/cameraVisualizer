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


def main():
    print("start.")

    _, camera_params, _ = \
        read_files_replica(folder_path="data/Replica/", data_name="office0_original", delta=50)

    scale = 1
    camera_params[:, 3:6] *= scale

    ax = plt.figure().add_subplot(projection='3d')

    red = 300
    ax.plot(camera_params[:, 3], camera_params[:, 4], camera_params[:, 5], "o-", color="#A0A0A0", ms=1, linewidth=0.5)
    # ax.plot(camera_params[red, 3], camera_params[red, 4], camera_params[red, 5], "o", color="#aa0000", ms=5)

    for param in camera_params:
        rot = Rotation.from_rotvec(param[0:3])
        R = rot.as_matrix()
        #R = np.linalg.inv(R)
        t = param[3:6]

        coord = Coord(0.1, 1.0)
        coord.transform(R, t)
        coord.draw_coord(ax)

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

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    ax.view_init(elev=30, azim=260)

    plt.savefig("outputs/replica_office0_ori.png", format="png", dpi=300)
    plt.show()

    print(f"start: {camera_params[0, 3:6]}")
    print(f"end: {camera_params[-1, 3:6]}")

    print("end.")

if __name__ == "__main__":
    # print("opencv version: " + cv2.__version__)
    main()

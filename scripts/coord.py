import sys

import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d

class Coord:
    def __init__(self, length = 1.0, width = 0.7):
        self.length = length
        self.width = width
        self.root = np.array([0.0, 0.0, 0.0])
        self.pointedX = self.root + np.array([length, 0.0, 0.0])
        self.pointedY = self.root + np.array([0.0, length, 0.0])
        self.pointedZ = self.root + np.array([0.0, 0.0, length])
    
    def transform(self, R, t):
        self.root = R @ self.root
        self.pointedX = R @ self.pointedX
        self.pointedY = R @ self.pointedY
        self.pointedZ = R @ self.pointedZ

        self.root = self.root + t
        self.pointedX = self.pointedX + t
        self.pointedY = self.pointedY + t
        self.pointedZ = self.pointedZ + t

    def draw_coord(self, ax):
        xline = art3d.Line3D([self.root[0], self.pointedX[0]],[self.root[1], self.pointedX[1]],[self.root[2], self.pointedX[2]], color='red', linewidth=self.width)
        yline = art3d.Line3D([self.root[0], self.pointedY[0]],[self.root[1], self.pointedY[1]],[self.root[2], self.pointedY[2]], color='green', linewidth=self.width)
        zline = art3d.Line3D([self.root[0], self.pointedZ[0]],[self.root[1], self.pointedZ[1]],[self.root[2], self.pointedZ[2]], color='blue', linewidth=self.width)

        ax.add_line(xline)
        ax.add_line(yline)
        ax.add_line(zline)

    def get_coord(self, ax):
        xline = art3d.Line3D([self.root[0], self.pointedX[0]],[self.root[1], self.pointedX[1]],[self.root[2], self.pointedX[2]], color='red', linewidth=self.width)
        yline = art3d.Line3D([self.root[0], self.pointedY[0]],[self.root[1], self.pointedY[1]],[self.root[2], self.pointedY[2]], color='green', linewidth=self.width)
        zline = art3d.Line3D([self.root[0], self.pointedZ[0]],[self.root[1], self.pointedZ[1]],[self.root[2], self.pointedZ[2]], color='blue', linewidth=self.width)

        ax.add_line(xline)
        ax.add_line(yline)
        ax.add_line(zline)

        return 

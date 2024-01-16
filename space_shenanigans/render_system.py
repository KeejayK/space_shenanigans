from space_object import SpaceObject
from space_system import SpaceSystem


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Matplotlib shenanigans
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")


def draw_object(ax, position, radius, color, alpha):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = position[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = position[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = position[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x,y,z, color, alpha, 0)


# Set aspect ratio 
ax.set_box_aspect([1, 1, 1])

# Set axis labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Set plot limits
ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])
ax.set_zlim([-100, 100])



# Initialize objects
blue_planet = SpaceObject(
    5.97 * 10 ** 24, np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), "Blue"
)
red_planet = SpaceObject(
    2 * 10 ** 30, np.array([149.6 * 10 ** 6, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), "Red"
)

# Add objects to system
system = SpaceSystem([], 10)
system.objects.append(blue_planet)
system.objects.append(red_planet)
print(system)
system.euler_method()
print(system)


plt.show()

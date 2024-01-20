from space_object import SpaceObject
from space_system import SpaceSystem


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Matplotlib shenanigans
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")




def draw_object(space_object):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = space_object.position[0] + space_object.radius * np.outer(np.cos(u), np.sin(v))
    y = space_object.position[1] + space_object.radius * np.outer(np.sin(u), np.sin(v))
    z = space_object.position[2] + space_object.radius * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x,y,z, color=space_object.color)


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
blue_planet = SpaceObject(5, np.array([2,2,2]), np.array([0,0,0]) , np.array([0,0,0]), 5, "Blue")
red_planet = SpaceObject(20, np.array([50,50,50]), np.array([0,0,0]) , np.array([0,0,0]), 20, "Red")

# blue_planet = SpaceObject(
#     5.97 * 10 ** 24, np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), "Blue"
# )
# red_planet = SpaceObject(
#     2 * 10 ** 30, np.array([149.6 * 10 ** 6, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), "Red"
# )

# Add objects to system
system = SpaceSystem([], 10)
system.objects.append(blue_planet)
system.objects.append(red_planet)
print(system)
system.euler_method()
print(system)


draw_object(blue_planet)
plt.show()

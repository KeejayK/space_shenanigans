from space_object import SpaceObject
from space_system import SpaceSystem


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Matplotlib shenanigans
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")




def draw_object(space_object):
    """Draws SpaceObject in Matplotlib"""
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = space_object.position[0] + space_object.radius * np.outer(np.cos(u), np.sin(v))
    y = space_object.position[1] + space_object.radius * np.outer(np.sin(u), np.sin(v))
    z = space_object.position[2] + space_object.radius * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x,y,z, color=space_object.color)

def draw_objects(system):
    ax.clear()
    for space_object in system.objects:
        draw_object(space_object)

def system_positions(system):
    print("Positions:")
    for space_object in system.objects:
        print(space_object.position)

def system_velocities(system):
    print("Velocities:")
    for space_object in system.objects:
        print(space_object.velocity)    

def system_accelerations(system):
    print("Accelerations:")
    for space_object in system.objects:
        print(space_object.acceleration)

def system_properties(system):
    system_positions(system)
    system_velocities(system)
    system_accelerations(system)

def update(system):
    system_properties(system)
    system.euler_method()
    draw_objects(system)


# Set aspect ratio 
ax.set_box_aspect([1, 1, 1])

# Set axis labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Set plot limits
ax.set_xlim([-10000, 10000])
ax.set_ylim([-10000, 10000])
ax.set_zlim([-10000, 10000])



# Initialize objects
blue_planet = SpaceObject(500, np.array([200,200,200]), np.array([0,0,0]) , np.array([0,0,0]), 500, "Blue")
red_planet = SpaceObject(2000, np.array([5000,5000,5000]), np.array([0,0,0]) , np.array([0,0,0]), 2000, "Red")

# blue_planet = SpaceObject(
#     5.97 * 10 ** 24, np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), "Blue"
# )
# red_planet = SpaceObject(
#     2 * 10 ** 30, np.array([149.6 * 10 ** 6, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), "Red"
# )

# Add objects to system
system = SpaceSystem([], 100000)
system.objects.append(blue_planet)
system.objects.append(red_planet)

animation = FuncAnimation(fig, update, frames=range(5), interval=100)
plt.show()

# print("t=0")
# system_properties(system)
# system.euler_method()
# print("t=100")
# system_properties(system)
# system.euler_method()
# print("t=200")
# # system_properties(system)
# system.euler_method()
# print("t=300")
# # system_properties(system)
# system.euler_method()
# print("t=300")
# # system_properties(system)
# system.euler_method()
# # system_positions(system)  


# draw_object(blue_planet)
# draw_object(red_planet)
# plt.show()

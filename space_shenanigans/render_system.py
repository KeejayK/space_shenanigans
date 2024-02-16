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
    ax.set(xlim3d=(-10000, 10000), xlabel='X')
    ax.set(zlim3d=(-10000, 10000), zlabel='Z')
    ax.set(ylim3d=(-10000, 10000), ylabel='Y')
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
    # system_velocities(system)
    # system_accelerations(system)

# Set aspect ratio 
ax.set_box_aspect([1, 1, 1])
ax.set(xlim3d=(-10000, 10000), xlabel='X')
ax.set(zlim3d=(-10000, 10000), zlabel='Z')
ax.set(ylim3d=(-10000, 10000), ylabel='Y')




# Initialize objects
blue_planet = SpaceObject(500, np.array([200,200,0]), np.array([0,0,0]) , np.array([0,0,0]), 500, "Blue")
red_planet = SpaceObject(20000, np.array([0,0,0]), np.array([0,0,0]) , np.array([0,0,0]), 2000, "Red")

# blue_planet = SpaceObject(
#     5.97 * 10 ** 24, np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), "Blue"
# )
# red_planet = SpaceObject(
#     2 * 10 ** 30, np.array([149.6 * 10 ** 6, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), "Red"
# )


# Add objects to system
system = SpaceSystem([], 1000000)
system.objects.append(blue_planet)
system.objects.append(red_planet)


def update(frames):
    system_properties(system)
    system.euler_method()
    draw_objects(system)



animation = FuncAnimation(fig, update, frames=range(1000), interval=100)
plt.show()


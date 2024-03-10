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


def set_graph(bounds):
    """Re-establish graph bounds and aspect ratio (matplotlib shenanigans)"""
    ax.clear()
    ax.set_box_aspect([1, 1, 1])
    ax.set(xlim3d=(-bounds, bounds), xlabel='X')
    ax.set(zlim3d=(-bounds, bounds), zlabel='Z')
    ax.set(ylim3d=(-bounds, bounds), ylabel='Y')


def draw_objects(system, bounds):
    """Draw all objects in graph"""
    set_graph(bounds)
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




earth_mass = 5.972e24  # kg
sun_mass = 1.989e30 # kg
earth_sun_dst = 1.496e11  # m -> 1 AU
earth_orbital_velocity = np.sqrt(SpaceSystem.G * sun_mass / earth_sun_dst)  
bounds = 1.5 * earth_sun_dst


# Initialize objects
earth = SpaceObject(
    mass=earth_mass,
    position=np.array([earth_sun_dst, 0, 0]),  
    velocity=np.array([0, earth_orbital_velocity, 0]),  
    acceleration=np.array([0, 0, 0]),
    radius=1e10, 
    color="Blue"
)

sun = SpaceObject(
    mass=sun_mass,
    position=np.array([0, 0, 0]),  
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    radius=2.5e10,  
    color="Red"
)




# Add objects to system
system = SpaceSystem(objects = [], dt = 1e5)
system.objects.append(earth)
system.objects.append(sun)


def update(frames):
    system_properties(system)
    system.euler_method()
    draw_objects(system, bounds)



animation = FuncAnimation(fig, update, frames=range(1000), interval=100)
plt.show()


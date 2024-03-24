from space_object import SpaceObject
from space_system import SpaceSystem


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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
    
    
def draw_object_simple(space_object):
    ax.scatter(space_object.position[0], space_object.position[1], space_object.position[2], 
               color=space_object.color, s=100)


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
        # draw_object_simple(space_object)


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




system = SpaceSystem(objects = [], dt = 9e4)
sun_mass = 1.989e30 # kg

earth_mass = 5.972e24  # kg
earth_sun_dst = 1.496e11  # m -> 1 AU
earth_orbital_velocity = system.orbital_velocity(sun_mass, earth_sun_dst)

moon_mass = 7.348e22 # kg
moon_earth_dst = 3.844e8 # m
moon_orbital_velocity = system.orbital_velocity(earth_mass, moon_earth_dst)

mars_mass = 6.39e23 # kg
mars_sun_dst = 2.279e11
mars_orbital_velocity = system.orbital_velocity(sun_mass, mars_sun_dst)


# Initialize objects
earth = SpaceObject(
    mass = earth_mass,
    position = np.array([earth_sun_dst, 0, 0]),  
    velocity = np.array([0, earth_orbital_velocity, 0]),  
    acceleration = np.array([0, 0, 0]),
    radius = 0.5e10, # 6.378e6 too small to see
    color = "Blue"
)

moon = SpaceObject(
    mass = moon_mass,
    position = np.array([earth_sun_dst + moon_earth_dst, 0, 0]),  
    velocity = np.array([0, earth_orbital_velocity + moon_orbital_velocity, 0]),  
    acceleration = np.array([0, 0, 0]),
    radius = 0.1e10, 
    color = "Gray"
) 

sun = SpaceObject(
    mass = sun_mass,
    position = np.array([0, 0, 0]),  
    velocity = np.array([0, 0, 0]),
    acceleration = np.array([0, 0, 0]),
    radius = 5e10, 
    color="Yellow"
)

mars = SpaceObject(
    mass = mars_mass,
    position = np.array([mars_sun_dst, 0, 0]),   
    velocity = np.array([0, mars_orbital_velocity, 0]),
    acceleration = np.array([0, 0, 0]),
    radius = 0.75e10,  
    color="Red"
)



# Add objects to system
system.objects.append(earth)
system.objects.append(mars)
system.objects.append(moon)
system.objects.append(sun)



bounds = 1.2 * earth_sun_dst # to see the planets, axis bounds should be larger than distance from earth to sun
def update(frames):
    system_properties(system)
    system.euler_method()
    draw_objects(system, bounds)


animation = FuncAnimation(fig, update, frames=range(1000), interval=100)
plt.show()


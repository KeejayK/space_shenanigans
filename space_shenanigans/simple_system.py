from render_system import RenderSystem
from space_object import SpaceObject
from space_system import SpaceSystem
import numpy as np


if __name__ == "__main__":
    # Define Constants
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


    # To see the planets, axis bounds should be larger than distance from mars to sun
    bounds = 1.2 * mars_sun_dst 

    # Run
    simulation = RenderSystem(system = system, simple = False, bounds = bounds, method = "euler")
    simulation.run()


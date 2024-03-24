### Overview
Simulates the orbits of planets using matplotlib for 3d visualization. Forces are calculated using Newton's law of universal gravitation. Positions, velocities, and accelerations can be discretized using either the [Euler](https://en.wikipedia.org/wiki/Euler_method) or fourth order [Runge-Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods) method. 

![An animated gif of a 3d graph of a blue planet and a red planet orbiting a large yellow sun. A small black moon orbits the blue planet.](https://raw.githubusercontent.com/KeejayK/space_shenanigans/main/simple_orbit.gif)

### Customization
- Celestial bodies are represented using SpaceObject instances and can be added or removed by adding to the systems.objects array
- SpaceObject parameters can be changed to reflect accurate mass, position, and acceleration.
- Planet visualization can be made more efficient using the draw_object_simple function
- Simulation granularity can be adjusted by changing the dt parameter passed to the SpaceSystem object

### Dependencies
This project was built using the following packages 
- [matplotlib](https://pypi.org/project/matplotlib/)
- [numpy](https://pypi.org/project/numpy/)
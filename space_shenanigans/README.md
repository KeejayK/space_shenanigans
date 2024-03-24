

### Overview
Simulates the orbits of planets using matplotlib for 3d visualization. Forces are calculated using Newton's law of universal gravitation. Positions, velocities, and accelerations can be discretized using either the [Euler](https://en.wikipedia.org/wiki/Euler_method) or fourth order [Runge-Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods) method.

### Customization
- Celestial bodies by creating SpaceObject instances and can be added or removed by adding to the systems.objects array
- SpaceObject parameters can be changed to reflect accurate mass, position, and acceleration. Radius is purely cosmetic and has no impact on physics
- Simulation granularity can be adjusted by changing the dt parameter passed to the SpaceSystem object

### Dependencies
This project was built using the following packages 
- [matplotlib](https://pypi.org/project/matplotlib/)
- [numpy](https://pypi.org/project/numpy/)
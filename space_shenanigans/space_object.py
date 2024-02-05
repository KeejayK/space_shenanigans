class SpaceObject:
    """An object in space.

    Attributes:
        mass: Object mass in kg
        position: Position vector
        velocity: Velocity vector
        acceleration: Acceleration vector
        radius: Radius in m
        color: Name of color
    """

    def __init__(self, mass, position, velocity, acceleration, radius, color):
        """Initializes object based on mass, position, velocity, acceleration, radius and color"""
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.radius = radius
        self.color = color

    def __str__(self):
        """Returns string representation of this SpaceObject"""
        return f"Planet has mass {self.mass}, position {self.position}, velocity {self.velocity}, acceleration {self.acceleration}, color {self.color}"

    def __repr__(self):
        """Returns printable representation of this SpaceObject"""
        return f"SpaceObject(mass={self.mass}, position={self.position}, velocity={self.velocity}, acceleration={self.acceleration}, color={self.color})"
    
    # blue_planet = SpaceObject(1, numpy.array([0, 1, 0]), numpy.array([0, 0, 0]), "Blue")
    # red_planet = SpaceObject(1, numpy.array([1, 0, 0]), numpy.array([0, 0, 0]), "Red")
    # print(blue_planet)
    # print(red_planet)
    # blue_planet.gravity(red_planet)
    # print(blue_planet)
    # print(red_planet)

import numpy as np


class SpaceSystem:
    """A system of objects in space.

    Attributes:
        objects: List of space_object entities in system
        dt: Increment of time to advance the system by
        G: Gravitational Constant
    """

    G = 6.67430e-11

    def __init__(self, objects, dt=100):
        self.objects = objects
        self.dt = dt

    def __str__(self):
        return f"Space system has objects: {self.objects} and has time increment {self.dt}"
    
    def __repr__(self):
        return f"SpaceSystem(objects={self.objects}, dt={self.dt}, G={self.G})"

    def gravitational_force(self, mass_1, mass_2, distance_vector):
        """Calculate gravitational force between two objects

        Args:
                mass_1: mass of object 1 in kg
                mass_2: mass of object 2 in kg
                distance: meters between the centers of object 1 and 2

        Returns:
                vector force attracting mass 1 to mass 2
        """

        distance_magnitude = np.linalg.norm(distance_vector)
        distance_normal = distance_vector / distance_magnitude
        force_magnitude = self.G * mass_1 * mass_2 / distance_magnitude**2
        return distance_normal * force_magnitude

    def attract(self, object_1, object_2):
        """Accelerate two objects towards each other due to gravity"""
        distance_vector = object_2.position - object_1.position
        force_vector = self.gravitational_force(
            object_1.mass, object_2.mass, distance_vector
        )
        object_1.acceleration = object_1.acceleration + force_vector / object_1.mass
        object_2.acceleration = object_2.acceleration - force_vector / object_2.mass

    def accelerate_objects(self):
        """Update acceleration for all objects in system"""
        for object_1 in self.objects:
            for object_2 in self.objects:
                if object_1 != object_2:
                    self.attract(object_1, object_2)

    def euler_method(self):
        """Calculate position and velocity of objects in system using Euler method"""
        self.accelerate_objects()
        for entity in self.objects:
            entity.position = entity.position + entity.velocity * self.dt
            entity.velocity = entity.velocity + entity.acceleration * self.dt

    def runge_kutta_method(self):
        """Calculate position and velocity of objects in system using Runge-Kutta method"""
        self.accelerate_objects()
        for entity in self.objects:
            k1 = entity.velocity * self.dt
            k2 = (entity.velocity + k1 / 2) * self.dt
            k3 = (entity.velocity + k2 / 2) * self.dt
            k4 = (entity.velocity + k3) * self.dt

            entity.position = entity.position + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            entity.velocity = entity.velocity + entity.acceleration * self.dt
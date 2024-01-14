import numpy as np

G = 6.67430e-11  

def gravitational_force(m1, m2, r):
    return G * m1 * m2 / r**2

def acceleration(f, m):
	return f / m

def final_velocity(v, a, dt): 
	return v + a * dt

def final_position(p, v, dt):
	return p + v * dt
	


	def update_objects(self):
		num_objects = len(self.objects)
		for i in range(num_objects):
			for j in range(i + 1, num_objects):
				self.accelerate_objects()
				i.velocity = i.velocity + i.acceleration * self.dt
				j.velocity = j.velocity + j.acceleration * self.dt


# def final_position(p, a, dt):
# 	return p + .5 * a * dt ** 2

def force_between_objects(distance_vector, mass_1, mass_2):
	distance_magnitude = np.linalg.norm(distance_vector)
	gravitational_force = gravitational_force(mass_1, mass_2, distance_magnitude)
	force_direction = distance_vector / distance_magnitude
	return force_direction * gravitational_force


    # def gravity(self, object):
    #     """Update acceleration due to gravity"""
    #     distance_vector = object.position - self.position
    #     distance_magnitude = numpy.linalg.norm(distance_vector)

    #     force_magnitude = self.mass * object.mass / (distance_magnitude**2)
    #     distance_normal = distance_vector / distance_magnitude
    #     force_vector = distance_normal * force_magnitude
    #     print(f"distance_vector: {distance_vector}")
    #     print(f"distance_magnitude: {distance_magnitude}")
    #     print(f"force_magnitude: {force_magnitude}")
    #     print(f"force_normal: {distance_normal}")
    #     print(f"force_vector: {force_vector}")

    #     acceleration = force_vector / self.mass
    #     print(f"acceleration: {acceleration}")

    #     self.velocity = self.velocity + acceleration
    #     object.velocity = object.velocity - acceleration
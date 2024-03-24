from space_object import SpaceObject
from space_system import SpaceSystem


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class RenderSystem:
    """Encapsulates the setup, updating, and visualization of the simulation of a system of space objects

    Attributes:
        fig: Figure object in Matplotlib that holds everything
        ax: 3d subplot that holds all relevant plot elements in 3d simulation
        simple: Boolean flag indicating whether the simulation should draw objects with 3d surfaces
        bounds: Size of the plot box in meters
        system: Space System object that contains all space objects
        method: Discretization method to be used (euler or runge_kutta)
    """

    def __init__(self, system, simple, bounds, method):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.simple = simple
        self.bounds = bounds
        self.system = system
        self.method = method


    def set_graph(self):
        """Establish graph bounds and aspect ratio. Must be re-established (matplotlib shenanigans)"""
        self.ax.clear()
        self.ax.set_box_aspect([1, 1, 1])
        self.ax.set(xlim3d=(-self.bounds, self.bounds), xlabel='X')
        self.ax.set(zlim3d=(-self.bounds, self.bounds), zlabel='Z')
        self.ax.set(ylim3d=(-self.bounds, self.bounds), ylabel='Y')

    def draw_object(self, space_object):
        """Draws SpaceObject in Matplotlib as 3d surface"""
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = space_object.position[0] + space_object.radius * np.outer(np.cos(u), np.sin(v))
        y = space_object.position[1] + space_object.radius * np.outer(np.sin(u), np.sin(v))
        z = space_object.position[2] + space_object.radius * np.outer(np.ones(np.size(u)), np.cos(v))
        self.ax.plot_surface(x,y,z, color=space_object.color)
    
        
    def draw_object_simple(self, space_object):
        """Draws SpaceObject in Matplotlib as scatter plot point"""
        self.ax.scatter(space_object.position[0], space_object.position[1], space_object.position[2], 
                color=space_object.color, s=100)

    def draw_objects(self):
        """Draw all objects onto the plot"""
        self.set_graph()
        if (self.simple):
            for space_object in self.system.objects:
                self.draw_object_simple(space_object) 
        else:
            for space_object in self.system.objects:
                self.draw_object(space_object)

    def system_positions(self):
        """Print all current positions of all objects in the system"""
        print("Positions:")
        for space_object in self.system.objects:
            print(space_object.position)

    def update(self, frames):
        """Update system a single step using method specified upon initialization"""
        self.system_positions()
        if (self.method == "euler"):
            self.system.euler_method()
        elif (self.method == "runge_kutta"):
            self.system.runge_kutta_method()
        self.draw_objects()

    def run(self):   
        """Run simulation""" 
        animation = FuncAnimation(self.fig, self.update, frames=range(1000), interval=100)
        plt.show()




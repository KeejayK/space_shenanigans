import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from space_object import SpaceObject
from space_system import SpaceSystem



# class Render:
#     def __init__(self, size):
#         fig, ax = plt.subplots(1, 1, subplot_kw={"projection": "3d"})
#         self.size = size
#         self.objects = []
#         self.figure = fig
#         self.ax = ax

# x = Render(100)
# x.add()
# plt.show()


blue_planet = SpaceObject(
    5.97 * 10 ** 24, np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), "Blue"
)
red_planet = SpaceObject(
    2 * 10 ** 30, np.array([149.6 * 10 ** 6, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0]), "Red"
)
system = SpaceSystem([], 10)
system.objects.append(blue_planet)
system.objects.append(red_planet)
print(system)
system.euler_method()
print(system)





fig, ax = plt.subplots(1, 1, subplot_kw={"projection": "3d"})
ax.plot((0,0,0), marker='0',markersize=.5,color='yellow')


# ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=400)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import de_plotter

#Global Variables

total_time = 25
e = 0.1
initial_x = 1
initial_v = 0
w = 1

# Creating lists for plotting points

# x- coordinate
time_list = np.arange(0, total_time + e, e)

# Plotting positions of each case on Y coordinate
plt.plot(time_list, de_plotter.coordinate_points(total_time, initial_x, initial_v, e, "-x"), 'r', label="x^1")
plt.plot(time_list, de_plotter.coordinate_points(total_time, initial_x, initial_v, e, "-x**3"), 'b', label="x^3")
plt.plot(time_list, de_plotter.coordinate_points(total_time, initial_x, initial_v, e, " -x**5"), 'g', label="x^5")

# formatting graph

plt.legend()
plt.title('Comparing different Harmonic Motions')
plt.xlabel('time (1 unit = π)')
plt.ylabel('position (x) (seconds)')
plt.grid()

# Tick marks on x-axis

i = 0
x_tick_list = []
while np.pi * i <= total_time:
    x_tick_list.append(np.pi * i)
    i += 1
plt.xticks(x_tick_list)

# Showing Graph

plt.show()


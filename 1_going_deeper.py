import matplotlib
matplotlib.use("agg")  # Anti-Grain Geometry Engine
import numpy as np
import matplotlib.pyplot as plt


# figures hold axes; axes hold almost everything else
fig = plt.figure()
ax = fig.gca()  # get current axes

# creating data
x = np.linspace(-6, 6, 500)
y = np.sinc(x)

ax.plot(x, y)

fig.savefig("images/curve.png")

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


timestamp = (356,297,290,275,298,321,334,338,326)
distance = (171,353,446,537,605,693,803,892,944)
data = np.array((timestamp, distance))
print(timestamp(2))

tck, u = interpolate.splprep(data, s=0)
unew = np.arange(0, 1.01, 0.01)
out = interpolate.splev(unew, tck)

plt.xlim(0, 818)
plt.ylim(0, 1090)
plt.xlabel('X Axis limit is (0,7)')
plt.ylabel('Y Axis limit is (-0.5,4)')
plt.plot(out[0], out[1], color='orange')
plt.plot(data[0, :], data[1, :], 'ob')
plt.show()

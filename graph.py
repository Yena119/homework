import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0, 10, 0.01)
sy = np.sin(time)
cy = np.cos(time)
plt.figure('그래프이름')
plt.plot(time, sy, label='sin')
plt.plot(time, cy, label='cos')
plt.legend()
plt.xlabel('time')
plt.ylabel('value')
plt.title('sin cos Graph')
plt.grid()
plt.show()


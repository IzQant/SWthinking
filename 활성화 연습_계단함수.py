import numpy as np
import matplotlib.pyplot as plt
def step(x):
    #y = x > 0
    #return y.astype(np.int)
    return np.array(x > 0, dtype=np.int64)

x = np.arange(-5.0, 5.0, 0.1)
y = step(x)

fig = plt.figure(figsize=(8,8))
fig.set_facecolor('white')

plt.plot(x,y)
plt.ylim(-0.5, 1.5)
plt.xlim(-5, 5)
plt.ylabel('y', fontsize = 20, rotation = 0)
plt.xlabel('x', fontsize = 20)
plt.title("Step Function", fontsize = 30)
plt.show()



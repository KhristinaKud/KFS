import matplotlib.pyplot as plt
import numpy as np

def lorenz(xyz, *, s=10, r=28, b=2.667):
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])
dt = 0.01
num_steps = 5000

xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = (0.1, 0.1, 0.1)
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
t = np.arange(0, (num_steps + 1)*dt, dt)
plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.plot(t, xyzs[:, 0], 'b')
plt.xlabel('Час')
plt.ylabel('X')
plt.subplot(3, 1, 2)
plt.plot(t, xyzs[:, 1], 'g')
plt.xlabel('Час')
plt.ylabel('Y')
plt.subplot(3, 1, 3)
plt.plot(t, xyzs[:, 2], 'r')
plt.xlabel('Час')
plt.ylabel('Z')
plt.tight_layout()
plt.show()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot( projection='3d')
ax.plot(*xyzs.T, lw=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Атрактор Лоренца")
plt.show()

xyzs_perturbed = np.empty((num_steps + 1, 3))
xyzs_perturbed[0] = (0.01, 0.1, 0.1)  # Зміна на 0.1%
for i in range(num_steps):
    xyzs_perturbed[i + 1] = xyzs_perturbed[i] + lorenz(xyzs_perturbed[i]) * dt

plt.figure(figsize=(15, 10))
plt.subplot(3, 1, 1)
plt.plot(t, xyzs_perturbed[:, 0], 'b')
plt.xlabel('Час')
plt.ylabel('X')
plt.subplot(3, 1, 2)
plt.plot(t, xyzs_perturbed[:, 1], 'g')
plt.xlabel('Час')
plt.ylabel('Y')
plt.subplot(3, 1, 3)
plt.plot(t, xyzs_perturbed[:, 2], 'r')
plt.xlabel('Час')
plt.ylabel('Z')
plt.tight_layout()
plt.show()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot( projection='3d')
ax.plot(*xyzs.T, lw=0.5, label='Оригінал', color='b')
ax.plot(*xyzs_perturbed.T, lw=0.5, label='Зміна',color='g')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.show()
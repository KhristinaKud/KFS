import unittest
import numpy as np


def lorenz(xyz, *, s=10, r=28, b=2.667):
    x, y, z = xyz
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return np.array([x_dot, y_dot, z_dot])
dt = 0.01
num_steps = 5000
class TestLorenzAttractor(unittest.TestCase):

    def test_length(self):
        xyzs = np.empty((num_steps + 1, 3))
        xyzs[0] = (0.1, 0.1, 0.1)
        for i in range(num_steps):
            xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
        self.assertEqual(xyzs.shape[0], num_steps + 1)
        self.assertFalse(np.any(np.isnan(xyzs)) or np.any(np.isinf(xyzs)))# 5001
    def test_structure(self):
        xyzs = np.empty((num_steps + 1, 3))
        xyzs[0] = (0.1, 0.1, 0.1)
        for i in range(num_steps):
            xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
        self.assertEqual(xyzs.shape[1], 3)  #  X, Y, Z
    def test_different_initial_conditions(self):
        xyzs1 = np.empty((num_steps + 1, 3))
        xyzs1[0] = (0.1, 0.1, 0.1)
        xyzs2 = np.empty((num_steps + 1, 3))
        xyzs2[0] = (0.01, 0.1, 0.1)
        for i in range(num_steps):
            xyzs1[i + 1] = xyzs1[i] + lorenz(xyzs1[i]) * dt
            xyzs2[i + 1] = xyzs2[i] + lorenz(xyzs2[i]) * dt
        self.assertFalse(np.allclose(xyzs1[-1], xyzs2[-1]))


if __name__ == "__main__":
    unittest.main()

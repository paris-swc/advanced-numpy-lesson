import numpy as np 
import matplotlib.pyplot as plt

# generate sample data

centers = np.array([[2, 3],
                    [3, 2],
                    [2.8, 3]])
noise = 0.1 * np.random.randn(10, 3, 2)

clusters = noise + centers
data = clusters.reshape(30, 2)
np.random.shuffle(data)

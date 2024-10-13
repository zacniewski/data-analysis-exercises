import numpy as np
import matplotlib.pyplot as plt

from skimage import io

pic = np.array(io.imread('images/fire.jpeg'))
plt.imshow(pic)
plt.show()

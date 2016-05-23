import numpy as np
import pylab as pl
from matplotlib import colors

data = (np.random.rand(3, 5, 10) > 0.8).astype(np.int)
cdata = (data * np.arange(1, 4)[:, None, None]).sum(axis=0)
overlap = data.sum(axis=0) > 1
cdata[overlap] = 4

y, x = np.mgrid[:6, :11]

cmap = colors.ListedColormap(["w", "r", "g", "b", "k"])
pl.pcolormesh(x, y, cdata, edgecolor="black", cmap=cmap)
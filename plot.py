# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np

import sys
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
from scipy.interpolate import interpn


def density_scatter(x, y, ax=None, sort=True, bins=20, **kwargs):
    """
    Scatter plot colored by 2d histogram
    """
    if ax is None:
        fig, ax = plt.subplots()
    data, x_e, y_e = np.histogram2d(x, y, bins=bins, density=True)
    z = interpn((0.5 * (x_e[1:] + x_e[:-1]), 0.5 * (y_e[1:] + y_e[:-1])), data, np.vstack([x, y]).T, method="splinef2d",
                bounds_error=False)

    img = plt.imread("mirage" + ".png")
    ax.imshow(img, extent=[-3000, 2300, -2700, 1000])


    # To be sure to plot all data
    z[np.where(np.isnan(z))] = 0.0

    # Sort the points by density, so that the densest points are plotted last
    if sort:
        idx = z.argsort()
        x, y, z = x[idx], y[idx], z[idx]

    ax.scatter(x, y, c=z, cmap='viridis', **kwargs)

    norm = Normalize(vmin=np.min(z), vmax=np.max(z))
    # cbar = fig.colorbar(cm.ScalarMappable(norm=norm), ax=ax)
    # cbar.ax.set_ylabel('Density')

    plt.axis('off')

    plt.show()

    return ax


if "__main__" == __name__:

    if sys.argv[1] is not None:
        try:
            df = pd.read_csv(sys.argv[1])
            mapname = sys.argv.split('_')
        except IndexError:
            df = pd.read_csv("test_data.csv")
            pass

    plotx = df.get('x')
    ploty = df.get('y')

    density_scatter(plotx, ploty, bins=[10, 10])
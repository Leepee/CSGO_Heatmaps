# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import numpy as np
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
    df = pd.read_csv("test_data.csv")
    plotx = df.get('x')
    ploty = df.get('y')

    density_scatter(plotx, ploty, bins=[10, 10])

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# df = pd.read_csv("test_data.csv")
# # df.plot()  # plots all columns against index
# # df.plot(kind='scatter', x='x', y='y') # scatter plot
#
# # df.plot(kind='density')  # estimate density function
# # df.plot(kind='hist')  # histogram
#
#
#
# ax = df.plot.hexbin(x='x', y='y', gridsize=25, colormap='plasma')
#
# # plt.figure(figsize = (16,16))
# # plt.hist2d(x='x', y='y', bins=50, cmap=plt.cm.jet)
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# def extract_csv_gen_plot(csv_path):
#
#     data = pd.read_csv(csv_path, index_col=1)
#     data = data.drop(data.columns[[0, 1]], axis=1)
#     data.index.names = ['Name']
#     g = sns.heatmap(data)
#     g.set_yticklabels(g.get_yticklabels(), rotation=0)
#     g.set_title('Heatmap')
#     plt.tight_layout()
#     plt.show()
#
#
# extract_csv_gen_plot("test_data.csv")

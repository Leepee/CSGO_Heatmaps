import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df  = pd.read_csv("locations.csv")
# df.plot()  # plots all columns against index
# df.plot(kind='scatter', x='x', y='y') # scatter plot


# df.plot(kind='density')  # estimate density function
# df.plot(kind='hist')  # histogram

ax = df.plot.hexbin(x='x', y='y', gridsize=25, colormap='plasma')

# plt.figure(figsize = (16,16))
# plt.hist2d(x='x', y='y', bins=50, cmap=plt.cm.jet)
plt.show()














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
# extract_csv_gen_plot("locations.csv")
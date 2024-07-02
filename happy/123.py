import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()

# drop "Antarctica" and "Seven seas" from the dataframe (which will make our
# world map visualization a bit prettier)
drop_idxs = world["continent"].isin([
    "Antarctica",
    "Seven seas (open ocean)"
])
world = world.drop(world[drop_idxs].index)

# start by plotting a map of the world
world.boundary.plot(
    ax=ax,
    color="black",
    linewidth=0.5
)

# grab the unique set of continents, generate a unique color for each one,
# and initialize the list of patches
continents = world["continent"].unique()
colors = sns.color_palette("Set3", len(continents))
patches = []

# loop over the continent names and corresponding colors
for (continent_name, color) in list(zip(continents, colors)):
    # grab all countries that belong to the continent, then plot each of the
    # continents, giving each a unique color
    continent = world[world["continent"] == continent_name]
    continent.plot(ax=ax, color=color, alpha=0.5)

    # generate a patch for the current continent
    patch = mpatches.Patch(label=continent_name, color=color)
    patches.append(patch)

# add the patches to the map
# ax.legend(handles=patches, loc="lower left")

# turn off axis ticks
ax.set_xticks([])
ax.set_yticks([])

# set the plot title
# plt.title("Continents of the World with GeoPandas")
plt.show()
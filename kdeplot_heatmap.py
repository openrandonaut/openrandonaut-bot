# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np
import seaborn as sns
import matplotlib.colors as cols
import matplotlib.pyplot as plt
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import shutil
from scipy import stats


def alpha_cmap(cmap):
    my_cmap = cmap(np.arange(cmap.N))
    x = np.linspace(0, 1, cmap.N)
    my_cmap[:, -1] = x ** (0.5)
    my_cmap = cols.ListedColormap(my_cmap)

    return my_cmap


df = pd.read_csv("coordinates.csv")

BBox = (df.longitude.min(), df.longitude.max(), df.latitude.min(), df.latitude.max())


xs = df.longitude
ys = df.latitude


def get_densest_point(xs, ys):
    kernel = stats.gaussian_kde(np.vstack([xs, ys]), bw_method="silverman")
    # define grid.
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    x, y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    positions = np.vstack([x.ravel(), y.ravel()])

    k_pos = kernel(positions)

    max_dense_lat, max_dense_lon = positions.T[np.argmax(k_pos)]

    print(f"KDE cordinates: {max_dense_lat}, {max_dense_lon}")
    return max_dense_lon, max_dense_lat


minlat = BBox[2]
maxlon = BBox[0]
maxlat = BBox[3]
minlon = BBox[1]
print(f"minlat = {minlat}")
print(f"minlon = {minlon}")
print(f"maxlat = {maxlat}")
print(f"maxlon = {maxlon}")

# Use background image
# ruh_m = plt.imread("_map.png")

fig, ax = plt.subplots(figsize=(7.6, 7))

ax.set_title("4096 point Kernel Density Estimate heatmap")
ax.set_xlim(BBox[0], BBox[1])
ax.set_ylim(BBox[2], BBox[3])

plot = sns.kdeplot(
    x=xs,
    y=ys,
    fill=True,
    thresh=0.4,
    levels=100,
    cmap="rocket_r",
    alpha=0.5,
    linewidth=0.5,
    antialiased=True,
    zorder=1,
)

plot.collections[0].set_alpha(0)

# Use background image
# ax.imshow(ruh_m, zorder=0, extent=BBox, aspect="auto")

ax.scatter(df.longitude, df.latitude, zorder=1, alpha=0.2, c="b", s=10, marker=".")
densest_point_x, densest_point_y = get_densest_point(xs, ys)
ax.scatter(float(densest_point_y), float(densest_point_x), zorder=1, marker="x", c="r")

plt.show()

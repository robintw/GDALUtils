import numpy as np
from matplotlib.pyplot import plot
import rasterio.features
import gdal


def read_gdal_to_array(filename):
    im = gdal.Open(filename)

    return im.GetRasterBand(1).ReadAsArray()


def plot_segments(seg):
    all_coords_x = []
    all_coords_y = []

    for shp, val in rasterio.features.shapes(seg.astype(np.int16),
                                             connectivity=8, mask=(seg > 0)):
        coords = list(zip(*shp['coordinates'][0]))
        all_coords_x.append(np.array(coords[0]) - 0.5)
        all_coords_y.append(np.array(coords[1]) - 0.5)

    for xs, ys in zip(all_coords_x, all_coords_y):
        plot(xs, ys, 'r', lw=5)

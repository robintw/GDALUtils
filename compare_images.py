#!/usr/bin/env python
import sys

import numpy as np
import gdal


def singleband_image_to_array(filename):
    img = gdal.Open(filename)

    arr = img.GetRasterBand(1).ReadAsArray()

    return arr


def compare(filename1, filename2):
    a1 = singleband_image_to_array(filename1)
    a2 = singleband_image_to_array(filename2)

    diff = a1 - a2

    diff = diff[np.isfinite(diff)]

    print("Image comparison:\n")
    print("Comparing:")
    print("\t %s" % filename1)
    print("\t %s" % filename2)
    print("")
    print("Min: %.10f" % diff.min())
    print("Mean: %.10f" % diff.mean())
    print("Median: %.10f" % np.median(diff))
    print("Max: %.10f" % diff.max())

    val = ((np.abs(diff) < 0.1).sum() / float(np.size(diff))) * 100.0
    print("perc diff < 0.01 %f" % val)

    # if np.allclose(a1, a2):
    #     print("All elements close according to np.allclose")
    # else:
    #     print("All elements NOT CLOSE according to np.allclose")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('USAGE: compare_images.py IMAGE1 IMAGE2')
        sys.exit(1)

    compare(sys.argv[1], sys.argv[2])

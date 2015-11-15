#!/usr/bin/env python
import sys

import numpy as np

from io import singleband_image_to_array


def compare_images(filename1, filename2):
    a1 = singleband_image_to_array(filename1)
    a2 = singleband_image_to_array(filename2)

    diff = a1 - a2

    diff = diff[np.isfinite(diff)]

    minval = diff.min()
    maxval = diff.max()
    meanval = diff.mean()
    medval = np.median(diff)

    print("Image comparison:\n")
    print("Comparing:")
    print("\t %s" % filename1)
    print("\t %s" % filename2)
    print("")
    print("Min: %.10f" % minval)
    print("Mean: %.10f" % meanval)
    print("Median: %.10f" % medval)
    print("Max: %.10f" % maxval)

    percval = ((np.abs(diff) < 0.01).sum() / float(np.size(diff))) * 100.0
    print("perc diff < 0.01 %f" % percval)

    # if np.allclose(a1, a2):
    #     print("All elements close according to np.allclose")
    # else:
    #     print("All elements NOT CLOSE according to np.allclose")

    return minval, meanval, medval, maxval, percval

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('USAGE: compare_images.py IMAGE1 IMAGE2')
        sys.exit(1)

    compare_images(sys.argv[1], sys.argv[2])

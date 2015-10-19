import gdal
import numpy as np
import pandas as pd


def image_to_df(filename, bands, nodata=-9999):
    """Reads the specified bands from the specified image and imports
    them to a pandas data frame.

    Parameters:

    * filename: Image filename to read (must be a GDAL-supported format) bands:
    * A list of bands to process. Band IDs are 1-based. For example [1, 2, 3]
    * for a standard Landsat image will process the Blue, Green and Red bands
    * nodata: A No Data value to ignore, defaults to -9999

    Returns: A pandas data frame with a column per band read, with all the data
    in it, with no data values removed. Columns will be named "Bx" where x is
    the band ID.

    """
    im = gdal.Open(filename)

    data = {}

    for band_id in bands:
        band = im.GetRasterBand(band_id).ReadAsArray().astype(float)

        band[band == nodata] = np.nan
        data['B%d' % band_id] = band.ravel()

    df = pd.DataFrame(data)

    df.dropna()

    return df

import gdal
import numpy as np
import pandas as pd

def image_to_df(filename, bands, nodata=-9999):
	im = gdal.Open(filename)

	data = {}

	for band_id in bands:
		band = im.GetRasterBand(band_id).ReadAsArray()

		band[band == nodata] = np.nan
		data['B%d' % band_id] = band.ravel()

	df = pd.DataFrame(data)

	df.dropna()

	return df
import gdal,gdalconst
import dateutil

def apply_fn_to_image(in_filename, f, out_filename, out_type):
	in_im = gdal.Open(in_filename)

	drv = in_im.GetDriver()

	out_im = drv.Create(out_filename, in_im.RasterXSize, in_im.RasterYSize, in_im.RasterCount, out_type)
	out_im.SetGeoTransform(in_im.GetGeoTransform())
	out_im.SetProjection(in_im.GetProjection())

	#out_im = drv.CreateCopy(out_filename, in_im)

	for band_id in range(1, in_im.RasterCount+1):
		in_band = in_im.GetRasterBand(band_id)

		arr = in_band.ReadAsArray()

		out_band = out_im.GetRasterBand(band_id)
		out_band.WriteArray(f(arr, band_id))

	del in_im
	del out_im

# in_filename = r"E:\_Datastore\Small_DMC.bsq"
# out_filename = r"E:\_Datastore\Small_DMC_ALTERED.bsq"

# apply_fn_to_image(in_filename, lambda x: x+100, out_filename)
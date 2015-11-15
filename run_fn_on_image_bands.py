import gdal


def apply_fn_to_image(in_filename, f, out_filename, out_type):
    """Applies the given function to each band of the input image and saves the
    result to the output filename.

    Parameters:

    * in_filename: Input image filename (must be a GDAL-supported type)
    * f: The function to apply to the image. Must take two arguments: array, band_id
    * out_filename: The filename to save the result to. The image will be saved
    in the same type as the input image.
    * out_type: The output type of the image, one of the gdalconst.GDT_XX constants

    The function which is passed will be called once for each band with two
    arguments:
    * array: an array containing the data for that band
    * band_id: the 1-based id of the band - allowing the function to operate differently
    for each band of an image. """

    in_im = gdal.Open(in_filename)

    drv = in_im.GetDriver()

    out_im = drv.Create(out_filename,
                        in_im.RasterXSize, in_im.RasterYSize,
                        in_im.RasterCount,
                        out_type)
    out_im.SetGeoTransform(in_im.GetGeoTransform())
    out_im.SetProjection(in_im.GetProjection())

    #out_im = drv.CreateCopy(out_filename, in_im)

    for band_id in range(1, in_im.RasterCount + 1):
        in_band = in_im.GetRasterBand(band_id)

        arr = in_band.ReadAsArray()

        out_band = out_im.GetRasterBand(band_id)
        out_band.WriteArray(f(arr, band_id))

    del in_im
    del out_im

import gdal
import gdalconst


def image_like(orig_im, output_filename, drv=None, datatype=None, nbands=None,
               xdim=None, ydim=None):
    # Can work when orig_im is a filename or a GDAL image
    if type(orig_im) == str:
        orig_im = gdal.Open(orig_im)
        need_to_close = True
    else:
        need_to_close = False

    # Can work when drv is a GDAL Driver or a string with a driver name
    # So, if a string, convert to a GDAL Driver
    if type(drv) == str:
        drv = gdal.GetDriverByName(drv)
    if type(drv) == gdal.Dataset:
        drv = drv.GetDriver()
    else:
        drv = orig_im.GetDriver()

    b = orig_im.GetRasterBand(1)

    if datatype is None:
        datatype = b.datatype
    else:
        if datatype == float:
            datatype = gdalconst.GDT_Float32
        elif datatype == int:
            datatype = gdalconst.GDT_Int32
        elif datatype == bool:
            datatype = gdalconst.GDT_Byte

    if nbands is None:
        nbands = orig_im.RasterCount

    if xdim is None:
        xdim = orig_im.RasterXSize

    if ydim is None:
        ydim = orig_im.RasterYSize

    new_im = drv.Create(output_filename, xdim, ydim, nbands, datatype)

    new_im.SetProjection(orig_im.GetProjection())
    new_im.SetGeoTransform(orig_im.GetGeoTransform())

    if need_to_close:
        del orig_im

    del b

    return new_im

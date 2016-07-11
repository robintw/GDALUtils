import gdal
from osgeo import gdalconst

def resample_raster(src_name,to_name,dst):
    """
    Resamples and reprojects raster 'src_name' to match raster 'to_name'.
    It stores the resulting raster in 'dst'.
    All the parameters are filepaths.
    """
    src = gdal.Open(src_name, gdalconst.GA_ReadOnly)
    src_proj = src.GetProjection()
    src_geotrans = src.GetGeoTransform()

    match_ds = gdal.Open(to_name, gdalconst.GA_ReadOnly)
    match_proj = match_ds.GetProjection()
    match_geotrans = match_ds.GetGeoTransform()
    wide = match_ds.RasterXSize
    high = match_ds.RasterYSize

    dst_filename = dst
    dst = gdal.GetDriverByName('GTiff').Create(dst_filename, wide, high, 1, gdalconst.GDT_Float32)
    dst.SetGeoTransform( match_geotrans )
    dst.SetProjection( match_proj)

    gdal.ReprojectImage(src, dst, src_proj, match_proj, gdalconst.GRA_Bilinear)

    dst = None # Flush
    return dst_filename

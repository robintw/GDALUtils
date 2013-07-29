# from osgeo import ogr
# from subprocess import call

# ds = ogr.Open("C:\_Work\LandsatAERONET\wrs2_descending.shp")
# lyr = ds.ExecuteSQL("SELECT * from wrs2_descending WHERE path=202 and row = 25")
# feat = lyr.GetNextFeature()
# env = feat.GetGeometryRef().GetEnvelope()

# print env[0], env[3], env[2], env[1]

# Just use this command:
# gdalwarp.exe -of GTiff -cutline C:\_Work\LandsatAERONET\wrs2_descending.shp -csql "SELECT * FROM wrs2_descending WHERE path=202 and row=25" -crop_to_cutline GLOBCOVER_L4_200901_200912_V2.3.tif Output.tif
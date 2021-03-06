# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")


# Local variables:
Properties_Projected_feet = "Properties_Projected_feet"
Properties_Projected_feet__2_ = "Properties_Projected_feet"
Properties_Projected_feet__3_ = "Properties_Projected_feet"
Properties_Projected_feet__4_ = "Properties_Projected_feet"
Properties_Projected_feet__5_ = "Properties_Projected_feet"
lu_1990 = "lu_1990"
lu_01 = "lu_01"
lu_2005 = "lu_2005"
lu_2010 = "lu_2010"
lu_2013 = "lu_2013"
v10m_buffer_Properties_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\10m_buffer_Properties.shp"
v300m_buffer_Properties_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\300m_buffer_Properties.shp"
v800m_buffer_Properties_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\800m_buffer_Properties.shp"
v1600m_buffer_Properties_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\1600m_buffer_Properties.shp"
v3200m_buffer_Properties_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\3200m_buffer_Properties.shp"
lu_1990__2_ = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\lu_1990"
lu_2001 = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\lu_2001"
lu_2005__3_ = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\lu_2005"
lu_2010__2_ = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\lu_2010"
lu_2013__2_ = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\lu_2013"
lu_recl_1990 = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu_recl_1990"
Reclass_lu_01 = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\Reclass_lu_01"
Reclass_lu_05 = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\Reclass_lu_05"
Reclass_lu_10 = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\Reclass_lu_10"
Reclass_lu_13 = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\Reclass_lu_13"
lu1990_recl_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu1990_recl.shp"
lu2001_recl_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu2001_recl.shp"
lu2005_recl_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu2005_recl.shp"
lu2010_recl_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu2010_recl.shp"
lu2013_recl_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu2013_recl.shp"
lu1990_recl_a_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu1990_recl_a.shp"
lu2001_recl_a_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu2001_recl_a.shp"
lu2005_recl_a_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu2005_recl_a.shp"
lu2010_recl_a_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu2010_recl_a.shp"
lu2013_recl_a_shp = "C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu2013_recl_a.shp"
lu1990_recl_a_Intersect = "C:\\Users\\Administrator\\Documents\\ArcGIS\\Default.gdb\\lu1990_recl_a_Intersect"

# Process: Buffer (2)
arcpy.Buffer_analysis(Properties_Projected_feet__2_, v300m_buffer_Properties_shp, "300 Meters", "FULL", "ROUND", "NONE", "")

# Process: Buffer (3)
arcpy.Buffer_analysis(Properties_Projected_feet__3_, v800m_buffer_Properties_shp, "800 Meters", "FULL", "ROUND", "NONE", "")

# Process: Buffer (4)
arcpy.Buffer_analysis(Properties_Projected_feet__4_, v1600m_buffer_Properties_shp, "1600 Meters", "FULL", "ROUND", "NONE", "")

# Process: Buffer (5)
arcpy.Buffer_analysis(Properties_Projected_feet__5_, v3200m_buffer_Properties_shp, "3200 Meters", "FULL", "ROUND", "NONE", "")

# Process: Polygon to Raster (2)
arcpy.PolygonToRaster_conversion(lu_01, "LANDUSE", lu_2001, "CELL_CENTER", "NONE", "10")

# Process: Reclassify (2)
arcpy.gp.Reclassify_sa(lu_2001, "LANDUSE", "1420 7;4300 3;1320 6;1222 5;1440 7;1240 10;1110 1;1330 6;1231 5;1232 5;1540 8;1520 8;1430 7;1310 6;1223 5;1130 2;1350 6;4110 3;1530 8;3100 10;1370 6;1360 6;1212 5;1560 8;4220 3;1250 5;3500 10;1511 8;5200 11;4210 3;1512 8;5100 11;3200 10;1340 6;3600 10;1120 3;3300 10;1550 8;1211 5;4120 3;1410 7;5300 11;1140 3;3400 10;2100 9", Reclass_lu_01, "DATA")

# Process: Raster to Polygon (2)
arcpy.RasterToPolygon_conversion(Reclass_lu_01, lu2001_recl_shp, "SIMPLIFY", "LANDUSE")

# Process: Calculate Areas (2)
arcpy.CalculateAreas_stats(lu2001_recl_shp, lu2001_recl_a_shp)

# Process: Polygon to Raster (3)
arcpy.PolygonToRaster_conversion(lu_2005, "LANDUSE", lu_2005__3_, "CELL_CENTER", "NONE", "10")

# Process: Reclassify (3)
arcpy.gp.Reclassify_sa(lu_2005__3_, "LANDUSE", "1420 7;4300 3;1320 6;1222 5;1440 7;1240 10;1110 1;1330 6;1231 5;1232 5;1540 8;1520 8;1430 7;1310 6;1223 5;1130 2;1350 6;4110 3;1530 8;3100 10;1370 6;1360 6;1212 5;1560 8;4220 3;1250 5;3500 10;1511 8;5200 11;4210 3;1512 8;5100 11;3200 10;1340 6;3600 10;1120 3;3300 10;1550 8;1211 5;4120 3;1410 7;5300 11;1140 3;3400 10;2100 9", Reclass_lu_05, "DATA")

# Process: Raster to Polygon (3)
arcpy.RasterToPolygon_conversion(Reclass_lu_05, lu2005_recl_shp, "SIMPLIFY", "LANDUSE")

# Process: Calculate Areas (3)
arcpy.CalculateAreas_stats(lu2005_recl_shp, lu2005_recl_a_shp)

# Process: Polygon to Raster (4)
arcpy.PolygonToRaster_conversion(lu_2010, "LANDUSE", lu_2010__2_, "CELL_CENTER", "NONE", "10")

# Process: Reclassify (4)
arcpy.gp.Reclassify_sa(lu_2010__2_, "LANDUSE", "1420 7;4300 3;1320 6;1222 5;1440 7;1240 10;1110 1;1330 6;1231 5;1232 5;1540 8;1520 8;1430 7;1310 6;1223 5;1130 2;1350 6;4110 3;1530 8;3100 10;1370 6;1360 6;1212 5;1560 8;4220 3;1250 5;3500 10;1511 8;5200 11;4210 3;1512 8;5100 11;3200 10;1340 6;3600 10;1120 3;3300 10;1550 8;1211 5;4120 3;1410 7;5300 11;1140 3;3400 10;2100 9", Reclass_lu_10, "DATA")

# Process: Raster to Polygon (4)
arcpy.RasterToPolygon_conversion(Reclass_lu_10, lu2010_recl_shp, "SIMPLIFY", "LANDUSE")

# Process: Calculate Areas (4)
arcpy.CalculateAreas_stats(lu2010_recl_shp, lu2010_recl_a_shp)

# Process: Polygon to Raster (5)
arcpy.PolygonToRaster_conversion(lu_2013, "LANDUSE", lu_2013__2_, "CELL_CENTER", "NONE", "10")

# Process: Reclassify (5)
arcpy.gp.Reclassify_sa(lu_2013__2_, "LANDUSE", "1420 7;4300 3;1320 6;1222 5;1440 7;1240 10;1110 1;1330 6;1231 5;1232 5;1540 8;1520 8;1430 7;1310 6;1223 5;1130 2;1350 6;4110 3;1530 8;3100 10;1370 6;1360 6;1212 5;1560 8;4220 3;1250 5;3500 10;1511 8;5200 11;4210 3;1512 8;5100 11;3200 10;1340 6;3600 10;1120 3;3300 10;1550 8;1211 5;4120 3;1410 7;5300 11;1140 3;3400 10;2100 9", Reclass_lu_13, "DATA")

# Process: Raster to Polygon (5)
arcpy.RasterToPolygon_conversion(Reclass_lu_13, lu2013_recl_shp, "SIMPLIFY", "LANDUSE")

# Process: Calculate Areas (5)
arcpy.CalculateAreas_stats(lu2013_recl_shp, lu2013_recl_a_shp)

# Process: Polygon to Raster
arcpy.PolygonToRaster_conversion(lu_1990, "LANDUSE", lu_1990__2_, "CELL_CENTER", "NONE", "10")

# Process: Reclassify
arcpy.gp.Reclassify_sa(lu_1990__2_, "Value", "1110 1;1130 2;1140 3;1210 5;1220 5;1230 5;1241 10;1242 10;1243 10;1250 5;1260 5;1311 6;1312 6;1313 6;1320 6;1330 6;1340 6;1360 6;1370 6;1380 6;1390 6;1410 7;1420 7;1430 7;1440 7;1510 8;1520 8;1530 8;1540 8;1550 8;1560 8;2000 9;3110 10;3120 10;3130 10;3210 10;3220 10;4110 3;4120 3;4210 3;4220 3;4300 3;5100 11;5200 11;5300 11;9999 11", lu_recl_1990, "DATA")

# Process: Raster to Polygon
arcpy.RasterToPolygon_conversion(lu_recl_1990, lu1990_recl_shp, "SIMPLIFY", "VALUE")

# Process: Calculate Areas
arcpy.CalculateAreas_stats(lu1990_recl_shp, lu1990_recl_a_shp)

# Process: Buffer
arcpy.Buffer_analysis(Properties_Projected_feet, v10m_buffer_Properties_shp, "10 Meters", "FULL", "ROUND", "NONE", "")

# Process: Intersect
arcpy.Intersect_analysis("C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\lu1990_recl_a.shp #;C:\\Users\\Administrator\\Desktop\\TDI_CapstoneProject\\Chicago_image\\Work_Flow_Property\\10m_buffer_Properties.shp #", lu1990_recl_a_Intersect, "ALL", "", "INPUT")


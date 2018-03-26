''' Author: Adrien Lepoutre 03/25/2018 (ahundredhuevos@gmail.com) - Hack Oregon 2018 Disaster Resilience Team '''


import rasterio
from rasterio.mask import mask
import geopandas as gpd
import os
import fiona
import matplotlib.pyplot as plot
import pandas as pd
from shapely.geometry import mapping
import numpy as np
from scipy.stats.kde import gaussian_kde
from scipy.stats import norm


#Inputs
vector_dir = '/Users/Caroline/Desktop/HACKOREGON/data_original/dogami_data/Hack_Oregon_Main_20180213/'
raster_dir = '/Users/Caroline/Desktop/HACKOREGON/data_original/dogami_data/Hack_Oregon_Rasters_20180213_TIFF/'

raster_name = "CSZ_M9p0_PGD_liquefaction_wet.tif"
polygon_id = 285




# Adjusting polygon id (objectids start at 1 vs 0 in Python)
polygon_id = 285 - 1

os.chdir(vector_dir)

#Read neighbordhood shapefile
nghd_main_shp  = gpd.read_file('RDPO_Earthquake_Impact_Analysis_Phase1.gdb', driver='FileGDB', layer='Neighborhood_Units')

# extract the geometry in GeoJSON format
nghd_geoms = nghd_main_shp.geometry.values # list of shapely geometries
geometry = nghd_geoms[polygon_id] # shapely geometry

# transform to GeJSON format
geoms_geJSON = [mapping(nghd_geoms[polygon_id])]

# extract the raster values values within the polygon
os.chdir(raster_dir)

with rasterio.open( raster_dir + raster_name) as src:
     out_image, out_transform = mask(src, geoms_geJSON, crop=False)


no_data=src.nodata
print no_data

# extract the values of the masked array
raster_data = out_image.data[0]
# extract the row, columns of the valid values
row, col = np.where(raster_data != no_data)
raster_data = np.extract(raster_data  != no_data,raster_data )

raster_df = pd.DataFrame(raster_data, columns = {"Raster_val"})

## Lines of code to get the frequency of values in a table
#unique, counts = np.unique(raster_data, return_counts=True)
#dict(zip(unique, counts))

#Create plot
plot.hist(raster_df.Raster_val, bins='auto')

plot.show()

print "Code ran successfully."

#Feel free to build onto this!!


#This is an option part to export the values back to a shapefile
# from rasterio import Affine # or from affine import Affine
# T1 = out_transform * Affine.translation(0.5, 0.5) # reference the pixel centre
# rc2xy = lambda r, c: (c, r) * T1
#
# d = gpd.GeoDataFrame({'col':col,'row':row,'CSZ_M9p0_pgv_site':CSZ_M9p0_PGD_liquefaction_wet})
# # coordinate transformation
# d['x'] = d.apply(lambda row: rc2xy(row.row,row.col)[0], axis=1)
# d['y'] = d.apply(lambda row: rc2xy(row.row,row.col)[1], axis=1)
# # geometry
# from shapely.geometry import Point
# d['geometry'] =d.apply(lambda row: Point(row['x'], row['y']), axis=1)
# # first 2 points
# d.head(2)
# # save to a shapefile
# d.to_file('/Users/Caroline/Desktop/HACKOREGON/data_original/dogami_data/Hack_Oregon_Main_20180213/CSZ_M9p0_PGD_liquefaction_wet.shp', driver='ESRI Shapefile')

#!/usr/bin/env python3
# Code name: get_mapsquare_rasterstats.py
# Brief description: Extract pixel value statistics from a (small) square box within a 
# a georeferenced raster file
# 
# Requirements: Python (3.6?)
#
# Start Date: 6/8/18
# Last Revision:
# Current Version:
# Notes:
#
# Copyright (C) 2018, Frederick D. Pearce, get_mapsquare_rasterstats.py

## Import modules
import gdal
import geopandas as gpd
import json
from osgeo import osr
import pandas as pd
from pyproj import Geod
from shapely.geometry import Polygon
# Import modules NOT included in "kitchen-sink", not sure about osgeo...
from rasterstats import zonal_stats

## Define functions
# ALL parameters defined in dictionary loaded from (default) json config file
def load_config(fname = "get_mapsquare_rasterstats_CONFIG.json"):
    with open(fname, "r") as f:
        params = json.load(f)
    return params

# Functions for building the map square as a shapely polygon
def calc_square_lonlat(lon_lat, xy_offset):
    """Calculate the longitude and latitude corresponding to the upper-right and lower-left
    corners of a square box centered on lat_lon, with a width of 2*xy_offset. 
    xy_offset MUST be in meters. Uses WGS84 (epsg=4326) ellipsoid.
    """
    az = [45, 225]
    lon = 2*[lon_lat[0]]
    lat = 2*[lon_lat[1]]
    mag = 2*[(2**0.5)*xy_offset]
    g = Geod(ellps='WGS84')
    rl_lon, tb_lat, _ = g.fwd(lon, lat, az, mag)
    return (rl_lon, tb_lat)

def calc_square_polygon(lon_lat, xy_offset):
    """Calculate polygon defining square box centered on lon, lat (decimal degrees)
    with a width of 2*xy_offset (meters).
    """
    rl_lon, tb_lat = calc_square_lonlat(lon_lat, xy_offset)
    poly = [Polygon((
            (rl_lon[0], tb_lat[0]),
            (rl_lon[0], tb_lat[1]),
            (rl_lon[1], tb_lat[1]),
            (rl_lon[1], tb_lat[0])
    ))]
    return poly

def get_geometry_from_point(lon_lat, xy_offset=300, xy_units="m"):
    """Returns a geodataframe containing a single geometry column that
    defines a square box centered on a point, specified as a lon, lat pair,
    The input parameter xy_offset defines the box half-width 
    1) Calculate the top-right corner and bottom-left corner of square box
    centered on lon_lat, using the WGS84 ellipsoid.
    2) Use the lon, lat of each corner to build a rectangular 
    polygon using shapely Polygon.
    3) Convert polygon to pandas geodataframe, set coordinate reference to 
    epsg 4326 (equivalent to WGS84).
    """
    if xy_units == "m":
        poly = calc_square_polygon(lon_lat, xy_offset)
        # Build geodataframe with one row, column
        gdf = gpd.GeoDataFrame(poly, columns=['geometry'], geometry='geometry')
        gdf.crs = {'init' :'epsg:4326'}
        return gdf
    else:
        print("Error: input xy_offset MUST be in meters!!!")

# Define functions for getting raster info/coordinate reference, and for 
# converting geometry to raster coordinate reference
def get_raster_nodatavalue(rasterfn):
    raster = gdal.Open(rasterfn)
    band = raster.GetRasterBand(1)
    return band.GetNoDataValue()

def get_raster_info_crs(raster_file, print_info=True):
    """Print information about raster file, and return its
    spatial reference system using gdal.
    """
    if print_info:
        try:
            print(gdal.Info(raster_file))
        except:
            print("Error reading info from raster file = {}".format(raster_file))
    try:
        raster = gdal.Open(raster_file)
    except:
        print("Error opening raster file = {}".format(raster_file))
    else:
        raster_crs = osr.SpatialReference()
        raster_crs.ImportFromWkt(raster.GetProjection())
        return raster_crs.ExportToProj4()

def transform_gdf_to_crsout(gdf, geom_col, crs_out):
    """Return copy of georeferenced polygon geometries from geopandas dataframe geometry 
    column, geom_col, transformed to the desired output Coordinate Reference, crs_out.
    """
    geom_out = gdf[geom_col].copy()
    return geom_out.to_crs(crs_out)

# Functions for computing raster stats, and for classifying raster stats
def get_raster_stats_df(geom_ras, df_index, raster_file, raster_name, **kwargs):
    """Compute raster statistics for input geometry and raster file.
    Return results in dataframe
    """
    kwargs.update({'nodata_value': get_raster_nodatavalue(raster_file)})
    #print(kwargs)
    geomstats = zonal_stats(geom_ras, raster_file, **kwargs)
    df_gs = pd.DataFrame(geomstats, index=df_index)
    df_gs.rename(columns={co: raster_name+'_'+co for co in df_gs.columns}, inplace=True)
    return df_gs

def get_geometry_raster_stats(gdf_merge, raster_params, **zonal_stats_params):
    for raster_name in raster_params['names']:
        # Step 3a 
        raster_file = raster_params['root'] + raster_name + raster_params['ext']
        #print("Computing statistics for raster file = {}".format(raster_file))
        raster_crs = get_raster_info_crs(raster_file, print_info=False)
        # Step 3b
        geom_ras = transform_gdf_to_crsout(gdf_merge, 'geometry', raster_crs)
        # Step 3c 
        gdf_merge = gdf_merge.join(
            get_raster_stats_df(
                geom_ras, gdf_merge.index, raster_file, raster_name, **zonal_stats_params
            )
        )
    return gdf_merge

def get_stats_classification(gdf, **kwargs):
    """Classify raster statistics using specified parameters in kwargs"""
    raster_names = [rn for rn in kwargs.keys() if rn != "stats_to_class"]
    for rn in raster_names:
        stats_to_class = [rn+'_'+sc for sc in kwargs['stats_to_class']]
        levels = kwargs[rn]['levels']
        labels = kwargs[rn]['level_labels']
        ctag = '_' + kwargs[rn]['class_tag']
        for s2c in stats_to_class:
            try:
                gdf[s2c+ctag] = pd.cut(gdf[s2c], levels, right=True, labels=labels)
            except KeyError:
                print("Key Error exception occurred for raster stat key = {}".format(s2c))
            except Exception as e:
                print("A non-key error exception occurred: {}".format(e))
    return gdf

def get_mapsquare_rasterstats(lon, lat):
    """Perform stats calculation given an input longitude, lon, and latitude, lat,
    in decimal degrees (floats) by 
    1) Loading parameters from config file, 
    2) Building a square box in lon/lat reference system (WGS84), 
    3) Looping through each input raster file to
        a) Extract the raster's spatial reference info, and (optionally) print info about it 
        b) Generate a single polygon (a square box) that is transformed from its initial 
        coordinate reference system (WGS84) to the crs used in the raster file, raster_crs
        c) Use rasterstats to compute analytics on pixel values within square box
        d) Append the statistics from each raster into a master, merged geodataframe
    4) Classifying a subset of the geometry statistics (optional), converting the calculated
        stat in pixel values to a label describing the stats intensity bin (e.g. "low", "high"),
        then append each of these additional columns to merged geodataframe, gdf_merge
    5) Outputing results: currently writes final geodataframe, gdf_merge, to csv file, and/or
        returns geojson output.
    """
    # Step 1
    params = load_config()
    # Step 2
    gdf_merge = get_geometry_from_point([lon, lat], **params['geometry']['from_point'])
    # Steps 3a-3d: repeat stats calculation for each raster file, append all results to gdf_merge
    gdf_merge = get_geometry_raster_stats(gdf_merge, params['raster'], **params['zonal_stats'])
    # *Hack job: After loop, compute total deformation for wet season
    gdf_merge['PGD_total_wet_mean'] = gdf_merge['PGD_landslide_wet_mean'] + gdf_merge['PGD_liquefaction_wet_mean']
    # Step 4
    if 'stats_classification' in params:
        gdf_merge = get_stats_classification(gdf_merge, **params['stats_classification'])
        #gdf_merge.info()
    # Step 5
    if 'write_csv' in params:
        gdf_merge.to_csv(params['write_csv']['name'])
    if 'return_json' in params:
        return gdf_merge.to_json()
    elif 'return_dict' in params:
        return gdf_merge.to_dict()
    elif 'return_geodf' in params:
        return gdf_merge

## If run from command line, execute script below here
if __name__ == "__main__":
    lon = -122.6263038077892
    lat = 45.4585072924327
    print(get_mapsquare_rasterstats(lon, lat))
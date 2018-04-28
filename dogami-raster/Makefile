# Setup:
#   - Create a source directory with all original tif files
#   - Install gdal 2.x and mbutil
#   - Run `make mbtiles` to create the mbtile intermediate format
#   - Run `make jpgs` to create the jpg filesystem tree structure
#     (this requires having first created the mbtiles)
#   - Run `make` to run both mbtiles and jpgs
.PHONY: mbtiles jpgs

count:
  echo $$(ls source/*.tif | wc -l) "layers found in the source directory";

# Uses gdal_translate to convert every geotiff file in the source
# directory into an mbtiles file. Then uses gdaladdo to create
# "overview" tiles, (i.e., tiles for zooming out).
mbtiles:
  mkdir -p mbtiles;
  for file in $$(find source -name *.tif); do \
    name=$$(basename $$file .tif); \
    echo "Converting " $$name " to mbtiles"; \
    gdal_translate $$file mbtiles/$$name.mbtiles -of MBTILES -ot CFloat32; \
    echo "Building zoom levels for " $$name; \
    gdaladdo -r average mbtiles/$$name.mbtiles 2 4 8 16 32 64; \
  done

# Uses mb-util to transform the original mbtiles file into a tree
# structure of jpg files so no webserver needs to be running to
# decode the mbtiles format. Jpgs in this structure can be requested
# straight from S3 or any fileserver.
jpgs:
  mkdir -p tiles;
  for file in $$(find mbtiles -name *.mbtiles); do \
    name=$$(basename $$file .mbtiles); \
    echo "Making jpg tiles for " $$name; \
    mb-util $$file --image_format=jpg tiles/$$name/; \
  done

# Assumes the awscli is already set up with an access token that has write access to
# the hacko-data-archive bucket.
sync:
  aws s3 sync tiles s3://hacko-data-archive/2018-disaster-resilience/dogami-raster

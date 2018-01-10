# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:59:42 2018

@author: dvalters

Creates a 0/1 landsea mask in NetCDF format
from a given input file, assuming that NODATA
values are sea, and everything else is land.

"""

from netCDF4 import Dataset
import numpy as np
import time

dataset = Dataset('/home/dvalters/Datasets/WFDEI_global_dyn.month.2d.gpp_gb.2000.1.nc',
                  format='NETCDF4_CLASSIC')
                 
# print the netcdf file format type
print(dataset.file_format)

for key, value in dataset.variables.items():
    print(key)

# print the variables in the netcdf dataset
# i.e. the 'fields' as some meteorologists call them...
print(dataset.variables)

# print all the dimensions in the dataset
for dimobj in dataset.dimensions.values():
    print(dimobj)

# prints the lat and longitude dimensions, and their size
lat = dataset.dimensions['lat']
lon = dataset.dimensions['lon']

print(dataset.dimensions['lat'])
print(dataset.dimensions['lon'])

#print the variable, GPP (gross primary production)
print(dataset.variables['gpp'])

# print any data storage conventions used (e.g. CF-1.5)
print(dataset.Conventions)

# Get a list of any attributes in the dataset (global attributes)
for attr in dataset.ncattrs():
    print(attr, '=', getattr(dataset, attr))

# Assign the variable GPP to an object name
GPP = dataset.variables['gpp']

# Get a list of variable attributes for GPP
for attr in GPP.ncattrs():
    print(attr, '=', getattr(GPP, attr))

# Create a new netcdf file to be used as the land sea mask

landsea = Dataset('/home/dvalters/Datasets/landsea_proj.nc', 'w', format='NETCDF4_CLASSIC')
print(landsea.file_format)

# Our landsea mask file should have the same dimensions as the input data
landsea_lat = landsea.createDimension('north_south', len(lat))
landsea_lon = landsea.createDimension('east_west', len(lon))
landsea_time = landsea.createDimension('time', None)

# Now create the coordinate variables
landsea_lats = landsea.createVariable('latitude', np.float64, ('north_south'))
landsea_lons = landsea.createVariable('longitude', np.float64, ('east_west'))
landsea_times = landsea.createVariable('time', np.float64, ('time',))

landsea_mask = landsea.createVariable('LANDMASK', np.float64, ('north_south', 'east_west'))
# Add some relevant attributes.
landsea_mask.standard_name = "LANDMASK"
landsea_mask.units = ""
landsea_mask.scale_factor = 1.0
landsea_mask.add_offset = 0.0
landsea_mask.missing_value = -9999.0
landsea_mask.vmin = 0.0
landsea_mask.vmax = 0.0
landsea_mask.num_bins = 0
# What about extents and DX?
# ...

landsea.description = 'Land-Sea mask with binary 0/1 values'
landsea.history = 'Created ' + time.ctime(time.time())
landsea.MAP_PROJECTION = "EQUIDISTANT CYLINDRICAL"
landsea.SOUTH_WEST_CORNER_LAT = -90.0
landsea.SOUTH_WEST_CORNER_LON = -180.0
landsea.DX = 0.5
landsea.DY = 0.5

landsea_lons.units = 'east_west'
landsea_lats.units = 'north_south'

# Now put some data into out variables
# lets do the lats and lons first

# Raw data values for lat and lon
lats = np.arange(-90,90,0.5)
lons = np.arange(-180,180,0.5)

# Now assign the raw data to netcdf coordinate variable
landsea_lons[:] = lons
landsea_lats[:] = lats 

# Making the mask
"""
Ok, so we need to read the GPP values from the input netcdf file,
then use this to create a binary mask where any data value is one and 
any nodata value is 0
"""

landsea_mask_array = landsea_mask[:]
input_data_array = GPP[:]

# Get the mask from the input array
# Note, a feature of netcdf-python is that it by default
# returns a masked array when loading variables. The mask
# is true where nodata or missing_value are present, as defined
# by the attributes of the variable.
mask = np.ma.getmask(input_data_array)

# Flip the boolean values, then convert them to 1s and zeros
landsea_mask_oneszeros = np.bitwise_not(mask).astype(int)

# Now write it into the netcdf object, save and close
landsea_mask[:] = landsea_mask_oneszeros

# We should close the two files now
dataset.close()
landsea.close()


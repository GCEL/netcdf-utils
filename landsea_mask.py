# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 10:59:42 2018

@author: dvalters

Creates a 0/1 landsea mask in NetCDF format
from a given input file, assuming that NODATA
values are sea, and everything else is land.

"""

from netCDF4 import Dataset

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

# prints the lat an longitude dimensions, and their size
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

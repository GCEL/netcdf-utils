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
                  'w', format='NETCDF4_CLASSIC')
                  
print(dataset.file_format)

#for key, value in dataset.variables.items():
#    print(key)

#level = dataset.createDimension('level)
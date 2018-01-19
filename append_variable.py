# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:18:02 2018

@author: dvalters
"""

from netCDF4 import Dataset
import numpy as np

dataset = Dataset('/home/dvalters/Datasets/WFDEI_global_dyn.month.2d.gpp_gb.2000.1.nc',
                  format='NETCDF4_CLASSIC')
                  

var_times = dataset.createVariable('time', np.int64, ('time',))


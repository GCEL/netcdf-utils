# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:34:29 2018

Plot some netcdf output from the LVT test cases

@author: dvalters
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

nc_file = './LVT_RCORR_FINAL.200612310000.d01.nc'
#nc_file = '/disk/scratch/local/dvalters/LVT/LVT_latest_7.2/STATS/LVT_MEAN_FINAL.201012310000.d01.nc'
#File handle
fh = Dataset(nc_file, mode='r')

lons = fh.variables['longitude'][:]
lats = fh.variables['latitude'][:]
soilmoist_vs_nvdi = fh.variables['SoilMoist_v_NDVI'][:]

soilmoist_vs_nvdi_units = fh.variables['SoilMoist_v_NDVI'].units

# Get some parameters for the Stereographic Projection
#lon_0 = lons.mean()
#lat_0 = lats.mean()

m = Basemap(width=5000000,height=3500000,
            resolution='l',projection='cyl')

# If our lat and longs were 1D, we would need to meshgrid them
# here to create 2D arrays.
"""
lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)
"""

# Plot Data
#cs = m.pcolor(lons,lats,np.squeeze(soilmoist_vs_nvdi))
cs = m.imshow(soilmoist_vs_nvdi, cmap='RdYlGn', vmin=-1.0, vmax=1.0)

# Add Grid Lines
m.drawparallels(np.arange(-90., 90., 30.), labels=[1,0,0,0], fontsize=16)
m.drawmeridians(np.arange(-180., 181., 60.), labels=[0,0,0,1], fontsize=16)

# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
#m.drawstates()
#m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label("Raw Correlation", fontsize=18)

# Add Title
plt.title('Soil Moisture (ESA CCI) vs NDVI (GIMMS)', fontsize=28)

plt.show()

# Masking a netCDF variable with a landsea mask

# We have a netCDF variable that has zero values for all the sea points, but we need
# all the sea points to be set to the mask value (i.e. the _FillValue in netCDF parlance)

# We also have a landsea mask separate file (landsea.nc), where land values are 1 and sea values are zero

# We want to mask the variable gpp_gb in the main netcdf file.

# 1. First copy over the landsea mask variable from landsea.nc to the file to be masked
ncks -A -v lsmask landsea.nc CARDAMOM_2001_2010_GPP_Mean_monthly_dayssince2001.nc

# 2. Then make sure that the variable in the other file (gpp) has a _FillValue set correctly
# (using -9999 here, but any convention will do (not zero though...)
ncatted -a _FillValue,gpp_gb,o,f,-9999 CARDAMOM_2001_2010_GPP_Mean_monthly_dayssince2001.nc

# 3. Then use ncap2 to set all the gpp values to _FillValue (the mask) whereever the landsea mask
# is not land (i.e. not == 1) 
ncap2 -s 'where(lsmask != 1) gpp_gb=gpp_gb@_FillValue' CARDAMOM_2001_2010_GPP_Mean_monthly_dayssince2001.nc CARDAMOM_2001_2010_GPP_Mean_monthly_dayssince2001_masked.nc

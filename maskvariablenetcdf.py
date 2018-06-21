from netCDF4 import Dataset
import numpy as np
import xarray as xr

def mask_plainnetcdf():
    with Dataset(mask_file, 'r') as mask, Dataset(input_file, 'a') as to_mask:
        for var in to_mask.variables:
            if len(to_mask[var].shape) == 4:  # The dimensions are time,depth,lat,lon
                for i in range(0, to_mask[var].shape[0]):
                    to_mask[var][i, :, :, :] = ma.masked_where(
                        np.logical_not(np.array(mask['tmask'][0, :, :, :], dtype=bool)),
                        np.array(to_mask[var][i, :, :, :]))[:]

def mask_xarray(var, landseamask_var='tmask'):
    with xr.open_dataset(mask_file) as m_f, xr.open_dataset(input_file) as i_f:
        mask = m_f[landseamask_var][0,:].values
        #data = i_f[var].where(mask)
        i_f[var] = i_f[var].where(mask)

mask_file = "WFD-EI-LandFraction2d_1x1_updated.nc"
#input_file = "WFDEI_global_dyn.2d.monthly_timevar_latfix.nc"
input_file = "CARDAMOM_2001_2010_GPP_Mean_monthly_dayssince2001.nc"

data = mask_xarray("gpp_gb", "lsmask")

#outfile = Dataset(data, 'w')





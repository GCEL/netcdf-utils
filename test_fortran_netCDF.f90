! Program used to test the Fortran netCDF libraries and
! debug an issue with a problem JULES netCDF file
program test_netcdf
use netcdf
implicit none

integer :: ncId, rhVarId, status
real    :: rhValue

status = nf90_open("JULES_WFDEI_global_dyn_ALL.nc", nf90_NoWrite, ncid)
if (status /= nf90_NoErr) call handle_err(status)

status = nf90_inq_varid(ncid, "latitude", rhVarId)
if (status /= nf90_NoErr) call handle_err(status)

status = nf90_get_var(ncid, "latitude", rhVarId)
if (status /= nf90_NoErr) call handle_err(status)

end program test_netcdf

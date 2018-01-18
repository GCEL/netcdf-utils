! An example of using nf90_get_var to read a netCDF 
! variable whose dimensions are the transpose of the
! Fortran 90 array
program transpose_nf90
use netcdf
use handle_error

implicit none
integer                            :: ncid, rhVarId, status
integer, parameter                 :: numLons = 144, numLats = 73
real, dimension(numLons, numLats)  :: rhValues
! netCDF varible has dimensions (numLons, NumLats)

status = nf90_open("/disk/scratch/local/dvalters/netcdf_test/ECMWF_ERA-40_subset.nc", &
       nf90_NoWrite, ncid)
if (status /= nf90_NoErr) call handle_err('nf90_open err ', status)

status = nf90_inq_varid(ncid, "lsp", rhVarId)
if(status /= nf90_NoErr) call handle_err('nf90_inq_var err ', status)

! Read transposed values: map vector would be (/ 1, numLats /) for
!   no transposition
status = nf90_get_var(ncid, rhVarId,rhValues) !, map = (/ numLons, 1 /))
if(status /= nf90_NoErr) call handle_err('nf90_get_var err: ', status)

end program transpose_nf90




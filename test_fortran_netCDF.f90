! Program used to test the Fortran netCDF libraries and
! debug an issue with a problem JULES netCDF file
! compile with:
! gfortran test_fortran_netCDF.f90 -I/usr/lib64/gfortran/modules/ -lnetcdff -lnetcdf -o test.out
program test_netcdf
use netcdf
implicit none

integer :: ncId, rhVarId, status
real    :: rhValue

status = nf90_open("JULES_WFDEI_global_dyn_ALL.nc", nf90_NoWrite, ncid)
if (status /= nf90_NoErr) call handle_err('nf90_open', status)

status = nf90_inq_varid(ncid, "latitude", rhVarId)
if (status /= nf90_NoErr) call handle_err('nf90_inq_varid', status)

status = nf90_get_var(ncid, rhVarId, rhValue, start = (/4, 3, 3 /))
if (status /= nf90_NoErr) call handle_err('nf90_get_var', status)

contains
  subroutine handle_err(funcname, status)
    character(len=*)    ::  funcname
    integer          ::  status
    print *, 'ERR: Calling ', funcname, ' returned error code: ', status
  end subroutine handle_err

end program test_netcdf

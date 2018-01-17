! Program used to test the Fortran netCDF libraries and
! debug an issue with a problem JULES netCDF file
! compile with:
! gfortran test_fortran_netCDF.f90 -I/usr/lib64/gfortran/modules/ -lnetcdff -o test.out
program test_netcdf
use netcdf
implicit none

integer :: ncid, rhVarId, status
! IDs for the x and y dims
integer :: xId, yId
! lengths of the x and y IDs
integer :: nx, ny
real    :: rhValue
! Some arrays for the variables
real, allocatable    :: lat(:,:)


! try opening the file
status = nf90_open("/disk/scratch/local/dvalters/netcdf_test/0.5-degree/JULES_WFDEI_global_dyn_ALL.nc", nf90_NoWrite, ncid)
if (status /= nf90_NoErr) call handle_err('nf90_open', status)

! Try reading the 'latitude' variable
status = nf90_inq_varid(ncid, "latitude", rhVarId)
if (status /= nf90_NoErr) call handle_err('nf90_inq_varid', status)

! Read a specific array value from a netcdf file (4,3,3)
status = nf90_get_var(ncid, rhVarId, rhValue, start = (/1, 1, 1 /))
if (status /= nf90_NoErr) call handle_err('nf90_get_var', status)

! Get the dimension ID for x
status = nf90_inq_dimid(ncid, 'x', xId)
if (status /= nf90_NoErr) call handle_err('nf90_inq_dimid', status)

! Get the dimension for x, the return assigns it to nx
status = nf90_inquire_dimension(ncid, xId, len=nx)
if (status /= nf90_NoErr) call  handle_err('nf90_inquire_dimension', status)

print *, "DIMENSION X:", ncid, rhVarId, rhValue, xId, nx

! Read a variable into an x,y array
!allocate(lat(nx,ny))

contains
  subroutine handle_err(funcname, status)
    character(len=*)    ::  funcname
    integer          ::  status
    print *, 'ERR: Calling ', funcname, ' returned error code: ', status
  end subroutine handle_err

end program test_netcdf

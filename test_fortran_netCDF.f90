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
status = nf90_open( &
   "/disk/scratch/local/dvalters/netcdf_test/0.5-degree/JULES_WFDEI_month_single_withTime_2010_12.nc", &
    nf90_NoWrite, ncid)
if (status /= nf90_NoErr) call handle_err('nf90_open', status)

! Try reading the 'latitude' variable
status = nf90_inq_varid(ncid, "latitude", rhVarId)
if (status /= nf90_NoErr) call handle_err('nf90_inq_varid', status)

! Read a specific array value from a netcdf file (4,3,3)
status = nf90_get_var(ncid, rhVarId, rhValue, start = (/1, 1, 1 /))
if (status /= nf90_NoErr) call handle_err('nf90_get_var', status)

! Get the dimension ID for x
status = nf90_inq_dimid(ncid, 'x', xId)
if (status /= nf90_NoErr) call handle_err('nf90_inq_dimid x', status)

! Get the dimension for x, the return assigns it to nx
status = nf90_inquire_dimension(ncid, xId, len=nx)
if (status /= nf90_NoErr) call  handle_err('nf90_inquire_dimension x', status)


print *, "DIMENSION X:", ncid, rhVarId, rhValue, xId, nx


! Get the dimension ID for y 
status = nf90_inq_dimid(ncid, 'y', yId)
if (status /= nf90_NoErr) call handle_err('nf90_inq_dimid y', status)

! Get the dimension for x, the return assigns it to nx
status = nf90_inquire_dimension(ncid, yId, len=ny)
if (status /= nf90_NoErr) call  handle_err('nf90_inquire_dimension y', status)

print *, "DIMENSION Y: ", ncid, rhVarId, rhValue, yId, ny

! Read a variable into an x,y array
allocate(lat(nx,ny))

status = nf90_get_var(ncid, rhVarId, lat)
if (status /= nf90_NoErr) call handle_err('nf90_get_var LAT into array', status)




end program test_netcdf

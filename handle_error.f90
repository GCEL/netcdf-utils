module handle_error
contains
  subroutine handle_err(funcname, status)
    character(len=*)    ::  funcname
    integer          ::  status
    print *, 'ERR: Calling ', funcname, ' returned error code: ', status
  end subroutine handle_err
end module handle_error

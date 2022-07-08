# Explain the results
x = 5
x == 5 and 3
#3
#True and 'Anything' returns 'Anything', but not converted to 'bool'
x == 4 and 3
#False
#False and 'Anything' returns 'False', 'Anything' is not checked,
3 and x == 5
#True
#'Anything' and True returns 'True'
3 and x == 4
#False
#'Anything' and False returns 'False'
isinstance(True, int)
#True
#'isinstance' is testing for types of objects. True is coded as '1', is an integer
isinstance(True, bool)
#True
#True is a boolean

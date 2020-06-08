def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1,number+1,1):
        print("{0:d}".format(i).rjust(width,' '), end='')
        print("{0:o}".format(i).rjust(width+1,' '), end='')
        print("{0:X}".format(i).rjust(width+1,' '), end='')
        print("{0:b}".format(i).rjust(width+1,' '))

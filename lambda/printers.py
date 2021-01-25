"""
Demonstrates IIFE - Imediately Invoked Function Execution
"""


# A regular function
def guru( funct, *args ):
    """
    Takes a function pointer and its args then calls it together.

    :param funct:
    :param args:
    :return:
    """
    funct(*args)

def printer_one( arg ):
    '''
    Takes arg and prints it and then returns it,
    :param arg:
    :return:
    '''
    return print(arg)

def printer_two( arg ):
    '''
    Takes arg and prints it but does not return it,

    :param arg:
    :return:
    '''
    print(arg)

# Call a regular function
x1 = guru( printer_one, 'printer 1 REGULAR CALL')
x2 = guru( printer_two, 'printer 2 REGULAR CALL \n')

# Call a regular function through a lambda
x3 = guru(lambda: printer_one('printer 1 LAMBDA CALL'))
x4 = guru(lambda: printer_two('printer 2 LAMBDA CALL'))

print(x1,x2,x3,x4)


'''A module for demonstrating exceptions'''

def convert(s):
    '''Convert to an integer'''
    try:
        x = int(s)
        print('Conversion succeeded! x =', x)
    except ValueError:
        x = -1
        print('Conversion failed!')
    except TypeError:
        x = -1
        print('Conversion failed!')
    return x
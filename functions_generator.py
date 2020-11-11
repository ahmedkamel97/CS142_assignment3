from chomsky import convert_grammar
from cyk import parse

def fun_gen(function_generator: str) -> str:
    '''
    This function determines if a given input is in the language 
    If it belongs to the language then the function Auto- generates a python function
        param: The string that is checked for membership and coverted into a automated python code
        return: Python function
    '''
    
    if parse('./function_grammar.txt', function_generator) != True:
        print('Therefore, code cannot be generated')
    else:
        replace = function_generator.replace(' ', '')
        left, right = replace.split('=')
        print('def {}: \n  y = {} \n  return y'.format(left, right))

'''
The array function contains the test functions that our machine recognizes or not.
Recognizable functions:
    f ( x ) = x * 5
    f ( x , z ) = sin ( x * z )
    f ( x , z ) = ( x + z ) / 2 

Non Recognizable functions:
    x + y + z
    f ( a ) = a / 2
    g ( x ) = f ( z )
'''


function = ['f ( x ) = x * 5',
    'f ( x , z ) = sin ( x * z )',
    'f ( x , z ) = ( x + z ) / 2', 
    'x + y + z',
    'f ( a ) = a / 2',
    'g ( x ) = f ( z )',
]

for i in function:
    print(i,':')
    fun_gen(i)
    print('')

import typing
from typing import List
from CNF import read_grammar, convert_grammar
import random
END   = None
debug = 1

"""
This is the main parser function
I used some online resources to build this parser function, the resources are cited within the references section 
"""
def parse(grammar_file_path: List[str], sentence: str) -> bool:
    grammar = convert_grammar(grammar_file_path)
    new_string = sentence.split()
    length = len(new_string)
    matrix = [[[] for x in range(length)] for y in range(length)]

    for word in range(length):
        for rule in grammar:
            if rule[1] == "\'%s\'" % new_string[word]:
                matrix[0][word].append(rule[0])

    for words_to_consider in range(2, length + 1):
        for start_cell in range(0, length - words_to_consider + 1):
            for left_size in range(1, words_to_consider):
                right_size = words_to_consider - left_size
                for rule in grammar:
                    if [x for x in matrix[left_size - 1][start_cell] if x == rule[1]]:
                        if [x for x in matrix[right_size - 1][start_cell + left_size] if x == rule[2]]:
                            matrix[words_to_consider - 1][start_cell].append(rule[0])

    sentence = grammar[0][0]
    
    if [n for n in matrix[-1][0] if n == sentence]:
        print("Belongs to the grammar")
        return True
    else:
        print("Does not belong to the grammar")
        return False


functions = ['f ( x ) = x * 5',
    'f ( x , z ) = sin ( x * z )',
    'f ( x , z ) = ( x + z ) / 2', 
    'x + y + z',
    'f ( a ) = a / 2',
    'g ( x ) = f ( z )',
]

for i in functions:
    print(i,':')
    parse('./math_grammar.txt', i)
    print('')

#------------------------------------------------------------------------------FUNCTION_Generator-----------------------------------------------------------------------

def fun_gen(function_generator: str) -> str:
    if parse('./math_grammar.txt', function_generator) != True:
        print('Therefore, code cannot be generated')
    else:
        replace = function_generator.replace(' ', '')
        left, right = replace.split('=')
        print('def {}: \n  y = {} \n  return y'.format(left, right))


for i in functions:
    print(i,':')
    fun_gen(i)
    print('')

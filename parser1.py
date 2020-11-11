#_______________________________________________________________________IMPORTING LIBRARIES & HELPER FUNCTIONS________________________________________________________
import typing
from typing import List
from CNF import read_grammar, convert_grammar
import random
END   = None
debug = 1
#________________________________________________________________________Sentences_Generator__________________________________________________________________________
"""
This function is used to generate correct sentences given any grammar
This function is used to test the parsing function later on
"""
def gen2(network, name) :
	net = network.get(name)
	if not net : return name     
	p = net[1]; s = ""
	while 1 :
		choose = random.randrange(len(p))
		s = s + " " + gen2(network, p[choose][0])
		next = p[choose][1]
		if next == END : return s
		p = net[next]

"""
This is even a simpler grammar than what we initially set to use for testing
This grammar is a subset of the original more complex grammar
"""
net3 = {
 'sentence': {
         1: (('subject', 2), ),
         2: (('verb', 3), ),
         3: (('articles', 4), ),
         4: (('noun'  ,  END), )
         },

 'noun'  : {
         1: (("Death",END),("Life",END),("Hate",END),("Failure",END))
         },
        
  'verb'  : {
         1: (("Accept",END),("Accuse",END),("Adapt",END),("Apologize",END))
         },
        
  'subject'  : {
         1: (("I",END),("You",END),("He",END),("She",END),("It",END),("We",END),("They",END))
         },

 'articles': {
         1: (("A",END),("An",END),("The",END))
         }
}

#___________________________________________________________________________Parser_Function___________________________________________________________________________

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

#__________________________________________________________________________________TESTING_______________________________________________________________________________

sentence_correct = [] 
for i in range(5):
    sentence_correct.append(gen2(net3, 'sentence'))

#print("Generated correct Sentences: ",sentence_correct, "\n")

sentence_wrong = ['I Drank The Coffee','We  Accuse  The  Lazy','They Burst Amidst An Bitter Then Angry Anxiety']

print("The correct sentences: \n")
for i in sentence_correct:
    print(i,':')
    parse('./english_grammar.txt', i)
    print('')

print("The wrong sentences: \n")
for i in sentence_wrong:
    print(i,':')
    parse('./english_grammar.txt', i)
    print('')







    

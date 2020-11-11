import typing
from typing import List

#I used some online resources to build these functions, the resources are cited within the references section 


"""
This function reads the grammar rules from a .txt file
"""
def read_grammar(file_path: str) -> List[str]:
    with open(file_path, 'r') as grammar_file:
        rules = grammar_file.readlines()
    return rules

"""
This function converts the grammar into CNF
"""
def convert_grammar(grammar_file_path: str) -> List[List[str]]:
    rules = read_grammar(grammar_file_path)
    grammar = []
    vert = "|"
    arrow = "->"
    for rule in rules:
        if "|" in rule:
            left, right = rule.split(arrow)
            left = [left.strip()]
            right_items = right.split(vert)
            for item in right_items:
                item_list = item.split()
                grammar.append(left + item_list)
        else:
            grammar.append(rule.replace(arrow, '').split())

    dictlist = {}
    unit_productions = []
    result = []
    index = 0

    for rule in grammar:
        new = []
        if len(rule) == 2 and rule[1][0] != "'":
            unit_productions.append(rule)
            if rule[0] in dictlist:
                dictlist[rule[0]] += [rule[1:]]
            else:
                dictlist[rule[0]] = [rule[1:]]
            continue
        elif len(rule) > 2:
            terminals = []
            for i in range(len(rule)):
                if rule[i][0] == "'":
                    terminals.append((rule[i], i))
            if terminals:
                for item in terminals:
                    rule[item[1]] = str(rule[0]) + str(index)
                    new.append([str(rule[0]) + str(index), item[0]])
                index += 1
            while len(rule) > 3:
                new.append([str(rule[0]) + str(index), rule[1], rule[2]])
                rule = [rule[0]] + [str(rule[0]) + str(index)] + rule[3:]
                index += 1
        if rule[0] in dictlist:
            dictlist[rule[0]] += [rule[1:]]
        else:
            dictlist[rule[0]] = [rule[1:]]
        result.append(rule)
        if new:
            for new_rule in new:
                result.append(new_rule)

    while unit_productions:
        rule = unit_productions.pop()
        if rule[1] in dictlist:
            for item in dictlist[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    result.append(new_rule)
                else:
                    unit_productions.append(new_rule)
                if rule[0] in dictlist:
                    dictlist[rule[0]] += [rule[1:]]
                else:
                    dictlist[rule[0]] = [rule[1:]]
    return result

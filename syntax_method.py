from basic_rules import *
from extended_rules import *

GRAMMAR = [
    RoofRule()
]

def analyze(items_list):
    done = False
    error = False
    for rule in GRAMMAR:
        applied = False
        i = 0
        while not applied and i < len(items_list)-1:
            applied = rule.apply(items_list[i:i+2])
            i += 1
        error = not applied
    return not error

def synthesize():
    pass

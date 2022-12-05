#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0]
    tup = length, first_char
    if sentence == ():
        first_char = None
    return(tup)

# random word generator used with AAWQ universe generator

import random
import string
# http://pythonfiddle.com/random-word-generator/ because I'm lazy and didn't feel like figuring this out myself

vowels = list('aeiou')

def gen_word(min, max):
    word = ''
    syllables = min + int(random.random() * (max-min))
    for i in range(0, syllables):
        word += gen_syllable()
    return word.capitalize()
def gen_syllable():
    ran = random.random()
    if ran < 0.333:
        return word_part('v')+ word_part('c')
    if ran < 0.666:
        return word_part('c') + word_part('v')
    return word_part('c') + word_part('v') + word_part('c')
def word_part(type):
    if type is 'c':
        return random.sample([ch for ch in list(string.ascii_lowercase) if ch not in vowels], 1)[0]
    if type is 'v':
        return random.sample(vowels, 1)[0]

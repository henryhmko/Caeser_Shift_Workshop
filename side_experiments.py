import random
import enchant

dictionary = enchant.Dict("en_US")

dictionary.check("???")
"""
>>> ord('h')
104
>>> ord('a')
97
>>> ord('^')
94
>>> chr(104)
'h'
>>> chr(97)
'a'
>>> chr(94)
'^'
"""

#make a function to create a big big number(more than 10 digits)
def big_num(digits):
    final_num = ''
    while digits:
        final_num += str(random.randint(1,9))
        digits -= 1
    return int(final_num)

def confusing_char():
    code = random.randint(46001, 48300)
    return chr(code)

def eng_to_kor_encoder(text):
    encoded = ''
    key = random.randint(45935, 48235)
    for letter in list(text):
        encoded += chr(ord(letter) + key)
    return encoded



def kor_encoder(text):
    encoded = ''
    for char in list(text): #for each korean character
        encoded += str(ord(char))
    return hex(int(encoded)) #convert to hexadecimal

def kor_decoder(text): #"text" should be without strings
    decoded = ''
    code = int(text)
    while code:
        char = code % (10 ** 5)
        decoded += chr(char)
        code //= 10 ** 5
    return decoded[::-1]

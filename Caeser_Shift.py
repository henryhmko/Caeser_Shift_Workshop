
import enchant
dictionary = enchant.Dict("en_US") #yay our very own dictionary

"""
Encode a program for converting normal text to Ceaser shift.
Arguments: str(normal text), shift
Output: str(decrypted text)

>>> caesar_encoder("abcd", 'a')
"abcd"

>>>caesar_encoder("abcd", 'c'):
"cdef"

>>>caesar_decoder('cdef', 'c'):
'abcd'

>>>caesar_shift("abcd", 'c', 'encode')
'cdef'

>>>caesar_shift('cdef', 'c', 'decode')
'abcd'

>>>advanced_caesar_decoder('td avib ozv wzno ozv')
'yi fang tea best tea'
"""

eng_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,
            'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16,
            'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}


def caesar_encoder(text, shift):
    text = text.lower()
    encoded_str = ''
    index = eng_dict[shift]
    for char in text:
        if char == ' ':
            encoded_str += ' '
        else:
            orig_i = eng_dict[char]
            new_char = list(eng_dict.keys())[list(eng_dict.values()).index((orig_i + index) % 26)]
            encoded_str += new_char
    return encoded_str


def caesar_shift(text, shift, action):
    text = text.lower()
    encoded_str = ''
    index = eng_dict[shift]
    if not(action == 'encode' or action == 'decode'):
        return "Invalid Command. Please Select 'encode' or 'decode'"
    for char in text:
        if char == ' ':
            encoded_str += ' '
        else:
            orig_i = eng_dict[char]
            if action == 'encode':
                new_char = list(eng_dict.keys())[list(eng_dict.values()).index((orig_i + index) % 26)]
            elif action == 'decode':
                new_char = list(eng_dict.keys())[list(eng_dict.values()).index((orig_i + (26 - index)) % 26)]
            encoded_str += new_char
    return encoded_str


def advanced_caesar_decoder(text):
    all_decipher = []

    for shift in eng_dict.keys():
        all_decipher.append(caesar_shift(text, shift, 'decode'))

    def correct_words_num(string):
        all_words = string.split() #splits text by whitespace
        valid_words = 0
        for word in all_words:
            if dictionary.check(word):
                valid_words += 1
        return valid_words #number of valid English words within the inputted text

    return max(all_decipher, key = correct_words_num) #return the decipher version with the most number of valid English words

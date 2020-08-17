# -*- coding: UTF-8 -*-
# Copyright (C) 2020 Aron Sarosi

from os.path import split
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

'''
Text Editing
'''
# Remove punctuations
def punctuation(text):
    for punct in string.punctuation:
        text = text.replace(punct, '')
    return text

# Remove common words
def common_words(text):
    stop_words = stopwords.words('english')
    for word in stop_words:
        text = text.replace(' ' + word + ' ', ' ')
    return text

# Remove numbers
def num_removal(text):
    if type(text) == str:
      for num in range(1, 10):
          text = text.replace(str(num), '')
      return text
    return False

def lower(text):
    return text.lower()


if __name__ == '__main__':
    print('Text edited')

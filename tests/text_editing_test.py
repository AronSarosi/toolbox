# -*- coding: UTF-8 -*-

# Import from standard library
import os
import toolbox
import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Import from our text_editing
from toolbox.text_editing import punctuation, common_words, lower, num_removal
import pytest


def test_punctuation():
   assert punctuation('*aloha!') == 'aloha'

def test_common_words():
    assert common_words('banana milkshake is yummy') == 'banana milkshake yummy'

def test_num_removal():
    assert num_removal('99 problems but I aint have 1') == ' problems but I aint have '
    assert num_removal(2) == False

def test_lower():
    assert lower('Markus') == 'markus'


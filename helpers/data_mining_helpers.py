import nltk
import re

"""
Helper functions for data mining lab session 2017 Fall

Notations:
d - document
D - documents
V - vowels
w - word
W - words
l - letter
"""
### \--> add new function:

def get_duplicated_place(row):
    if row == True:
        a = 1
    else:
        a = 0
    return a


### <--|

# def format_rows(docs):
#     """ format the text field and strip special characters """
#     D = []
#     for d in docs.data:
#         temp_d = " ".join(d.split("\n")).strip('\n\t')
#         D.append([temp_d])
#     return D

def format_labels(target):
    """ format the labels """
    label_name = ''
    if target == 0:
        label_name = 'negative'
    elif target == 1:
        label_name = 'positive'
    else:
        label_name = 'Something wrong!'
    return label_name

def check_missing_values(row):
    """ functions that check and verifies if there are missing values in dataframe """
    counter = 0
    for element in row:
        if element == True:
            counter+=1
    return ("The amoung of missing records is: ", counter)

def tokenize_text(text, remove_stopwords=False):
    """
    Tokenize text using the nltk library
    """
    tokens = []
    for d in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(d, language='english'):
            # filters here
            pattern = re.compile('\W')
            if pattern.match(word):
                continue
            else:
                tokens.append(word)
    return tokens

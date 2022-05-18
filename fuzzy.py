import pandas as pd
from operator import itemgetter
from numpy import array
from copy import deepcopy

'''
    Price :
        - Cheap
        - Moderate
        - Expensive

    Quality :
        - Worst
        - Bad
        - Average
        - Good
        - Best
'''

def read_data(filename):
    file = pd.read_excel(filename)
    data = file.to_numpy().copy()
    return data

# Price
def cheap_price(price):
    pass

def moderate_price(price):
    pass

def expensive_price(price):
    pass

# Quality
def worst_quality(quality):
    pass

def bad_quality(quality):
    pass

def average_quality(quality):
    pass

def good_quality(quality):
    pass

def best_quality(quality):
    pass

# Fuzzification
def price_fuzzy(price):
    pass

def quality_fuzzy(quality):
    pass

def inference(set_price, set_quality):
    pass

def sugeno(set_inference):
    pass

def sort_best_of_ten(set_sugeno, set_data):
    pass

if __name__=="__main__":
    print("Hello World!")
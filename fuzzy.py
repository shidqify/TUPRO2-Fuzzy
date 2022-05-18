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
    if price > 4:
        mu = 0.0
    elif 1 < price <= 4:
        mu = (-(price - 4)) / (4 - 1)
    elif price == 1:
        mu = 1.0
    return mu
    

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
    data = read_data("bengkel.xlsx")

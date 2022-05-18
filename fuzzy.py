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
    if price >= 4:
        mu = 0.0
    elif 1 <= price < 4:
        mu = (-1 * (price - 4)) / (4 - 1)
    return mu
    

def moderate_price(price):
    a = 3; b = 5; c = 8
    if price >= c or price <= a:
        mu = 0.0
    elif a < price <= b:
        mu = (price - a) / (b - a)
    elif b < price < a:
        mu = (-1 * (price - c)) / (c - b)
    return mu
    

def expensive_price(price):
    if price <= 7:
        mu = 0.0
    elif 7 < price <= 10:
        mu = (price - 7) / (10 - 7)
    return mu

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
    set_price = {
        "cheap"     : cheap_price(price),
        "moderate"  : moderate_price(price),
        "expensive" : expensive_price(price) 
    }

def quality_fuzzy(quality):
    set_quality = {
        "worst"     : worst_quality(quality),
        "bad"       : bad_quality(quality),
        "average"   : average_quality(quality),
        "good"      : good_quality(quality),
        "best"      : best_quality(quality)
    }

def inference(set_price, set_quality):
    pass

def sugeno(set_inference):
    pass

def sort_best_of_ten(set_sugeno, set_data):
    pass

if __name__=="__main__":
    data = read_data("bengkel.xlsx")

from calendar import c
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
def rumus(a,b,c,d,x):
    if x <= a and x >= d:
        return 0.0
    elif x > a and x < b:
        return (x-a)/(b-a)
    elif x >= b and x <= c:
        return 1.0
    elif x > c and x <= d:
        return -1*((x-d)/(d-c))


def worst_quality(quality):
    if  quality >= 30:
        return 0.0
    elif quality >= 1 and quality <= 20:
        return 1.0
    elif quality > 20 and quality <= 30:
        return -1*((quality-30)/(30-20))

def bad_quality(quality):
    return rumus(20,30,40,50,quality)

def average_quality(quality):
    return rumus(40,50,60,70,quality)

def good_quality(quality):
    return rumus(60,70,80,90,quality)

def best_quality(quality):
    if quality <= 80:
        return 0.0
    elif quality > 80 and quality < 90:
        return (quality-80)/(90-80)
    elif quality >= 90 and quality <= 100:
        return 1.0

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
    sugeno_set = []
    for i in range(len(data)):
        inference = inference(quality_fuzzy(data[i, 1]), price_fuzzy(data[i, 2]))
        sugeno_temp = sugeno(inference)
        sugeno_set.append([sugeno_temp, i+1])
    
    best_ten = sort_best_of_ten(sugeno_set, data)
    output = pd.DataFrame(best_ten, columns=['id', 'servis', 'harga', 'sugeno'])

    print(output)
    output.to_excel('urutan.xlsx', index = False)

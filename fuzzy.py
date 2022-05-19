from calendar import c
import pandas as pd
from operator import itemgetter
from numpy import array
from copy import deepcopy

'''
    Price :
        - Cheap     1 - 4
        - Moderate  3 - 8
        - Expensive 7 - 10

    Quality :
        - Worst     1 - 30
        - Bad       20 - 50
        - Average   40 - 70
        - Good      60 - 90
        - Best      80 - 100
'''

def read_data(filename):
    file = pd.read_excel(filename)
    data = file.to_numpy().copy()
    return data

# Price
def price_func(a,b,c,x):
    if x <= a and x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return -1 * (x - c) / (c - b)

def cheap_price(price):
    if price >= 5:
        mu = 0
    elif 3 < price <= 5:
        mu = (-1 * (price - 4)) / (4 - 1)
    elif 1 <= price <= 3:
        mu = 1
    return mu
    

def moderate_price(price):
    if price >= 8 or price <= 3:
        mu = 0
    elif 3 < price <= 5:
        mu = (price - 3) / (5 - 3)
    elif 5 < price <= 8:
        mu = (-1 * (price - 8)) / (8 - 5)
    return mu
    

def expensive_price(price):
    if price <= 5:
        mu = 0
    elif 5 < price <= 8:
        mu = (price - 5) / (8 - 5)
    elif price >= 8:
        mu = 1
    return mu

# Quality
def rumus(a,b,c,d,x):
    if x <= a and x >= d:
        return 0
    elif x > a and x < b:
        return (x-a)/(b-a)
    elif x >= b and x <= c:
        return 1
    elif x > c and x <= d:
        return -1 * ((x - d) / (d - c))


def worst_quality(quality):
    if  quality >= 30:
        return 0
    elif quality <= 20:
        return 1
    elif quality > 20 and quality <= 30:
        return -1 * ((quality - 30) / (30 - 20))

def bad_quality(quality):
    return rumus(20,30,40,50,quality)

def average_quality(quality):
    return rumus(40,50,60,70,quality)

def good_quality(quality):
    return rumus(60,70,80,90,quality)

def best_quality(quality):
    if quality <= 80:
        return 0
    elif quality > 80 and quality < 90:
        return (quality - 80) / (90 - 80)
    elif quality >= 90:
        return 1

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
    set_inference = {
        "low"   : [],
        "mid"   : [],
        "high"  : []
    }
    set_inference["low"].append(min(    set_price["cheap"],         set_quality["worst"]    ))
    set_inference["low"].append(min(    set_price["cheap"],         set_quality["bad"]      ))
    set_inference["low"].append(min(    set_price["cheap"],         set_quality["average"]  ))
    set_inference["low"].append(min(    set_price["cheap"],         set_quality["good"]     ))
    set_inference["low"].append(min(    set_price["moderate"],      set_quality["worst"]    ))
    set_inference["low"].append(min(    set_price["moderate"],      set_quality["bad"]      ))

    set_inference["mid"].append(min(    set_price["cheap"],         set_quality["best"]     ))
    set_inference["mid"].append(min(    set_price["moderate"],      set_quality["moderate"] ))
    set_inference["mid"].append(min(    set_price["moderate"],      set_quality["good"]     ))
    set_inference["mid"].append(min(    set_price["moderate"],      set_quality["best"]     ))
    set_inference["mid"].append(min(    set_price["expensive"],     set_quality["worst"]    ))
    set_inference["mid"].append(min(    set_price["expensive"],     set_quality["bad"]      ))
    set_inference["mid"].append(min(    set_price["expensive"],     set_quality["average"]  ))

    set_inference["high"].append(min(   set_price["expensive"],    set_quality["good"]      ))
    set_inference["high"].append(min(   set_price["expensive"],    set_quality["best"]      ))

    set_inference["high"]   = max(set_inference["high"])
    set_inference["mid"]    = max(set_inference["mid"])
    set_inference["low"]    = max(set_inference["low"])

    return set_inference

def sugeno(set_inference):
    high    = 100
    mid     = 60
    low     = 30

    top = ((set_inference["high"] * high) + (set_inference["mid"] * mid) + (set_inference["low"] * low))
    btm = set_inference["high"] + set_inference["mid"] + set_inference["low"]

    try:
        return top / btm
    except ZeroDivisionError:
        return 0

def sort_best_of_ten(set_sugeno, set_data):
    data = deepcopy(set_data)
    data.tolist()

    bestTen = []
    for i in range(10):
        best_bengkel = max(set_sugeno)
        index = best_bengkel[1] - 1
        bestTen.append([index+1, data[index][1], data[index][2], best_bengkel[0]])
        set_sugeno.remove(best_bengkel)
    
    bestTen.sort(key = itemgetter(3, 2, 1), reverse=True)
    return array(bestTen)    

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

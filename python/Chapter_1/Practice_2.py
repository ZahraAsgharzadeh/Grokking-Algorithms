"""
Page -> 12
Question 1.2 -> 
    تعداد اعضای لیست را دو برابر مقدار قبلی در نظر بگیرید .
    این بار حداکثر تعداد مراحل چقدر خواهد بود ؟
"""

# Answer 1.2

import math

def log(input) :
    return math.log(input, 2)
 
print(log(128*2)) 
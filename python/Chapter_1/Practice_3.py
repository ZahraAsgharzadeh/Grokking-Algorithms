"""
Page -> 22
Question 1.3 -> 
    زمان اجرا بر حسب 
    Big O ?
    ****************
    نام یک نفر را در نظر دارید و می خواهید شماره تلفن آن شخص را در دفترچه تلفن پیدا کنید .

    جستجوی دودویی

"""

# Answer 1.3

import math

def search(input) :
    return math.log(input, 2) # O (log n)
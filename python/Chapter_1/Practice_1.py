"""
Page -> 12 
Question 1.1 -> 
    فرض کنید یک لیست مرتب شده از 128 نام دارید، و با جست و جوی دودویی در میان آن لیست به جست و جو می پردازید.
    حداکثر تعداد مراحل چه مقدار خواهد بود ؟
"""

# Answer 1.1

import math

def log(input) :
    return math.log(input, 2)
 
print(log(128)) 
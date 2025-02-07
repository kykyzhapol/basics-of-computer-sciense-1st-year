from decimal import Decimal #this module for more accuracy

l_cm = Decimal(input())
l_inch = Decimal(l_cm * Decimal(1/2.54))
l_ft = Decimal(l_inch * Decimal(1/12))
l_yad= Decimal(l_ft * Decimal(1/3))
l_mil = Decimal(l_yad * Decimal(1/1760))
print(f'{l_yad} ярдов\n{l_mil} мили\n{l_ft} футов\n{l_inch} дюймов')
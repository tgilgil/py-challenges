"""Challenge 338"""

import math

def day_of_the_week_of(dd, mm, yyyy):
    """Uses Zeller's Algorithm from wikipedia to calculate day of the week"""
    return math.floor((dd + (((mm + 1) * 13) / 5) + yyyy + (yyyy / 4) - (yyyy / 100) + (yyyy / 400)) % 7)

def not_in_range_error(var_name):
    """return ValueError with invalid range message"""
    return ValueError(var_name + ' not between valid range')

DATE = input('Input date (eg "2017 10 30"):')

DATE_PARTS = DATE.split(' ')

YEAR = int(DATE_PARTS[0])
MONTH = int(DATE_PARTS[1])
DAY = int(DATE_PARTS[2])

DAYS = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

if (YEAR > 8000) or (YEAR < 0):
    raise not_in_range_error('year')

if (MONTH > 12) or (MONTH < 1):
    raise not_in_range_error('month')

if (DAY > 31) or (DAY < 1):
    raise not_in_range_error('day')

# Zeller's algorithm considers january & february as the 13th & 14th month of the previous year
if (MONTH == 1) or (MONTH == 2):
    YEAR -= 1

print(DAYS[day_of_the_week_of(DAY, MONTH, YEAR)])

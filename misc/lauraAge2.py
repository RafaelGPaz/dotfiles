#! /usr/bin/env python

from datetime import date

def calculate_age(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, day=born.day-1)
    if birthday > today:
        months_no =  (born.month + (today.month - born.month))
        years_no = (today.year - born.year - 1)
        if years_no > 1:
            y = 'years'
        else:
            y = 'year'
        if months_no > 1:
            m = 'months'
        else:
            m = 'month'
            
        print ("Laura is",years_no,y,'and',months_no,m)
    else:
        print ("Laura is",years_no,y,'and',months_no,m)

if __name__ == "__main__":
    day, month, year = [int(x) for x in "22/12/2012".split("/")]
    born = date(year, month, day)
    calculate_age(born)

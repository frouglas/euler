'''
Created on May 18, 2011

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is 
divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 
31 Dec 2000)?

ANSWER: 171

@author: frouglas
'''

def addWeek(day, month, year):
    if day < 22:
        return day + 7
    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return (day + 7) % 29
                else:
                    return (day + 7) % 28
            else:
                return (day + 7) % 29
        else:
            return (day + 7) % 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return (day + 7) % 30
    else:
        return (day + 7) % 31

day = 7
month = 1
year = 1900
count = 0

while year <= 2000:
    print(str(month) + '/' + str(day) + '/' + str(year))
    if day == 1:
        if year > 1900:
            count += 1
    newDay = addWeek(day, month, year)
    if day > newDay:
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
    day = newDay
print('There are ' + str(count) + " Sundays that fall on the first of the month between 1/1/1901 and 12/31/2000")
                 
    


# Days Between Dates (The Problem)

# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##

# def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    ##
    # return days

# MY ATTEMPTED ANSWER

"""def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True"""
    
# print isLeapYear(2002) 
# After several tests, this appears to be working!

"""def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    if y2 > y1:
        return "This is not valid input!" # birthdate must be before current date!
    days = 0
    for each in range(y2,y1 + 1): # I have decided that y2 is birthdate, y1 is todays date
        if isLeapYear(each) == True:
            days += 366
        else:
            days += 365
    # subtract days from 1/1 of birth year
    for birth_month in range(0,m2):
        days -= daysOfMonths[birth_month] 
    days += (daysOfMonths[m2 - 1] - d2)
    # subtract days between 12/31 and current date
    for current_month in range(m1 - 1,12):
        days -= daysOfMonths[current_month] # subtract entire current month
    days = days + d1 # add back days in current month
    return days

print daysBetweenDates(2016,10,20,1985,2,21) # correct answer is 11564
print daysBetweenDates(1985,10,20,2016,2,21) # checking defensive programming"""
# this seemed to work!

# Video Answer

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            return 28
        else:
            return 30

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
    year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates2(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
    and year2/month2/day2. Assumes inputs are valid dates, 
    and the first date is not after the second."""
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    # tests with 30day months
    assert daysBetweenDates2(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates2(2013, 1, 1, 2013, 1, 2) == 1
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2012, 12, 31) == (2013, 1, 1)
    assert nextDay(2013, 2, 28) == (2013, 3, 1)
    assert nextDay(2013, 9, 30) == (2013, 10, 1)
    assert daysBetweenDates2(2013, 1, 1, 2014, 1, 1) == 365
    assert nextDay(2012, 2, 28) == (2012, 2, 29)
    assert daysBetweenDates2(2012, 1, 1, 2013, 1, 1) == 366
    assert daysBetweenDates2(2013, 1, 24, 2013, 6, 29) == 156
    print "Tests finished."

test()

def test2():
    test_cases = [((2012, 1, 1, 2012, 2, 28), 58),
                   ((2012, 1, 1, 2012, 3, 1), 60),
                   ((2011, 6, 30, 2012, 6, 30), 366),
                   ((2011, 1, 1, 2012, 8, 8), 585),
                   ((1900, 1, 1, 1999, 12, 31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates2(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test2()

# This answer works, but might not be the best way
# There are lots of ways! Many are more efficient than this!







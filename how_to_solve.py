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

def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
# print isLeapYear(2002) 
# After several tests, this appears to be working!

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
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
print daysBetweenDates(1985,10,20,2016,2,21) # checking defensive programming
# this seemed to work!

# Video Answer




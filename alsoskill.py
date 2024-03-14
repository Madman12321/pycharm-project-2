def isLeapYear(year):
    '''
    Checks if year is a leap year.
    :param year: an integer representing a year value.
    :returns: True if year is a leap year; False otherwise
    :rtype: bool
    '''
    isLeap = False
    if year % 4 == 0 and year % 100 != 0:
        isLeap = True
    elif year % 100 == 0 and year % 400 == 0:
        isLeap = True
    return isLeap



def getDaysInMonth(month, year):
    '''
    Returns the number of days in a month.
    :param month: a month value between 1 and 12 representing January to December, respectively.
    :param year: the year for that month.
    :returns: Number of days in the month. If month does not fall in the range 1 to 12 inclusively, a -1 is returned.
    :rtype: integer
    '''
    for i in range(1, 13):
        if month == 1:
            return 31
        elif month == 2:
            return 28
        elif month == 3:
            return 31
        elif month == 4:
            return 30
        elif month == 5:
            return 31
        elif month == 6:
            return 30
        elif month == 7:
            return 31
        elif month == 8:
            return 31
        elif month == 9:
            return 30
        elif month == 10:
            return 31
        elif month == 11:
            return 30
        elif month == 12:
            return 31
        elif month != range(1, 13):
            return -1
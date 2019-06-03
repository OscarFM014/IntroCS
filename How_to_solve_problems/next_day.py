###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    """if month == 12 and day == 30: # my version
        month = 1
        day = 1
        year +=1
    else:
        if day == 30:
            day = 1
            month += 1
        else:
            day += 1

    return (year, month, day)"""

    if day < 30 :
        return year, month, day +1
    else:
        if month < 12:
            return year, month +1, 1
        else:
            return year+1, 1, 1

print nextDay(2012,4,30)

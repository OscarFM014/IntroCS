def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    b1 = year1 % 4
    resultado = 0
    sumar = 0
    if year1 == year2:
        if b1 == 0:
            daysofmonth = [31,29,31,30,31,30,31,30,31,30,31]
            if year1 == year2:
                if month1 == month2:
                    resultado = resultado + day2-day1
                else:
                    while month1 != month2:
                        a = daysofmonth[month1 - 1]
                        month1 = month1+1
                        sumar = (sumar + a)
                        resultado = (sumar + day2) - day1
            else:
                while year1 != year2:
                    if month1 == month2 and year1 != year2:
                        resultado = resultado + (365 - (day2-day1))
                        year1 = year1 + 1
                    else:
                        while month1 != month2:
                            a = daysofmonth[month1 - 1]
                            month1 = month1+1
                            sumar = (sumar + a)
                            resultado = resultado + (sumar + day2) - day1
        else:
            daysofmonth = [31,28,31,30,31,30,31,30,31,30,31]
            if year1 == year2:
                if month1 == month2:
                    resultado = resultado + day2-day1
                else:
                    while month1 != month2:
                        a = daysofmonth[month1 - 1]
                        month1 = month1+1
                        sumar = (sumar + a)
                resultado = resultado + (sumar + day2) - day1
            else:
                while year1 != year2:
                    if month1 == month2 and year1 != year2:
                        resultado = resultado + (366-(day2-day1))
                        year1 = year1 + 1
                    else:
                        while month1 != month2:
                            a = daysofmonth[month1 - 1]
                            month1 = month1+1
                            sumar = (sumar + a)
                        resultado = resultado + (sumar + day2) - day1
        return resultado
    else:
        if year1+1 == year2 and month1 == month2:
            if b1 == 0:
                if month1 == month2:
                    resultado = resultado + (365 - (day2-day1))
                    return resultado
            else:
                if month1 == month2:
                    resultado = resultado + (366 - (day2-day1))
                    return resultado
        if year1<year2:
            if year1%400 == 0:
                daysofmonth = [31,29,31,30,31,30,31,30,31,30,31]
                while month1 != month2:
                    a = daysofmonth[month1 - 1]
                    month1 = month1+1
                    sumar = (sumar + a)
                resultado = (sumar)+(day2 - day1)
                print resultado
            else:
                daysofmonth = [31,28,31,30,31,30,31,30,31,30,31]
                while month1 != month2:
                    a = daysofmonth[month1 - 1]
                    month1 = month1+1
                    sumar = (sumar + a)
                resultado = (sumar)+(day2 - day1)
        while year1<year2:
            year1=year1+1
            if year1%4 == 0:
                resultado= resultado + 366
            if year1%4 != 0:
                resultado= resultado + 365
        return resultado
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 0),
                  ((2012,1,1,2012,3,1), 0),
                  ((2011,6,30,2012,6,30), 0),
                  ((2011,1,1,2012,8,8), 0 ),
                  ((1900,1,1,1999,12,31), 0),
                  ((1997,10,7,2018,05,12), 0)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Tiene", daysBetweenDates(*args), "dias vividos"
        else:
            print "Tiene", daysBetweenDates(*args), "dias vividos"
test()

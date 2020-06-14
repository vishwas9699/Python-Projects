def isYearLeap(year):
    if year== 2000 or year==2016:
        return True
    else:
        return False

print(isYearLeap(1900))
print(isYearLeap(2016))


def daysInMonth(year, month):
    if year==2000 or year==2016:
        LeapMonthlist=[0,31,29,31,30,31,30,31,31,30,31,30,31]
        datemonth = LeapMonthlist[month]
        return datemonth



    elif year==1900 or year==1987:
        Monthlist=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        datemonth = Monthlist[month]
        return datemonth

    else:
        pass

print(daysInMonth(2000,2))

def dayOfYear(year, month, day):
    if year == 1900 or year == 1987:
        MonthList = [0,31,28,31,30,31,30,31,31,30,31,30,31] 
        DaysInYear = []
        daysInMonth = 0
        for i in range(0,366):
            DaysInYear.append(i)
        print(DaysInYear[365])
    #while MonthStop =< month
        monthgrab = [0,1,2,3,4,5,6,7,8,9,10,11,12]
        monthgo = monthgrab[month-1]

        MonthStop = 0
        for e in range(monthgrab[monthgo]):
            daysInMonth += MonthList[MonthStop]
            MonthStop += 1
        print(MonthStop)
        print(daysInMonth)
        correspondingDay = DaysInYear[day] + daysInMonth

        return correspondingDay
    elif year==2000 or year == 2016:
        MonthList = [0,31,29,31,30,31,30,31,31,30,31,30,31] 
        DaysInYear = []
        daysInMonth = 0
        for i in range(0,366):
            DaysInYear.append(i)
        print(DaysInYear[365])
    #while MonthStop =< month
        monthgrab = [0,1,2,3,4,5,6,7,8,9,10,11,12]
        monthgo = monthgrab[month-1]

        MonthStop = 0
        for e in range(monthgrab[monthgo]):
            daysInMonth += MonthList[MonthStop]
            MonthStop += 1
        print(MonthStop)
        print(daysInMonth)
        correspondingDay = DaysInYear[day] + daysInMonth

        return correspondingDay
    else:
        pass        


print("This is the ",dayOfYear(1987, 4, 20),"day of the year")
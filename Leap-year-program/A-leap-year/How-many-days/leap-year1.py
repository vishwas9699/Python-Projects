def isYearLeap(year):
    if isYearLeap==2000 or 2016:
        return True
    else:
        return False
    print(isYearLeap(1900))

    if year==2000:
        return True
    else:
        return False
    print(isYearLeap(1900))        


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
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
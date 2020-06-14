def isYearLeap(year):
    if year== 2000 or year==2016:
        return True
    else:
        return False

print(isYearLeap(1900))
print(isYearLeap(2016))


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
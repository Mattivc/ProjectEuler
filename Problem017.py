onesStrings = { 1 : "One", 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five", 6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine" }
tensString = { 1 : "Ten", 2 : "Twenty", 3 : "Thirty", 4 : "Forty", 5 : "Fifty", 6 : "Sixty", 7 : "Seventy", 8 : "Eighty", 9 : "Ninety" }
teensString = { 11 : "Eleven", 12 : "Twelve", 13 : "Thirteen", 14 : "Fourteen", 15 : "Fifteen", 16 : "Sixteen", 17 : "Seventeen", 18 : "Eighteen", 19 : "Nineteen"}

i = 0

for x in range(1, 1001):
	ones = x % 10
	tens = (x % 100 - ones)/10
	hundreds = (x % 1000 - tens)/100

	nString = ""
	if (x == 1000):
		nString += "OneThousand"
	else:
		if (hundreds != 0):
			nString += onesStrings[hundreds] + "Hundred"
			if (tens != 0 or ones != 0):
				nString += "And"
		teenNum = x % 100
		if (teenNum > 10 and teenNum < 20):
			nString += teensString[teenNum]
		else:
			if (tens != 0):
				nString += tensString[tens]
			if (ones != 0):
				nString += onesStrings[ones]
	print nString
	i += len(nString)
	

print(i)
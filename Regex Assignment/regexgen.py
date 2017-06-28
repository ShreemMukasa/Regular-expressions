import re


filename = "BigBend.csv"

total_string = ""

def sameThing(matches):
	for matchNum, match in enumerate(matches):
		    matchNum = matchNum + 1
		    
		    		    
		    for groupNum in range(0, len(match.groups())):
		        groupNum = groupNum + 1
		        
	return match.group(groupNum)

regex = r"<Object:<Path:/Databases/EGAPostBox/Rented/(P[A-Z]+[0-9]+)"
regex2 = r"Name:([A-Za-z]+)"
with open(filename,'r') as f:
	next(f)	

	for line in f:
		matches = re.finditer(regex, line)
		total_string += sameThing(matches)+","
		matches2 = re.finditer(regex2, line)
		total_string += sameThing(matches2)+"\r\n"
print total_string,


f.close()

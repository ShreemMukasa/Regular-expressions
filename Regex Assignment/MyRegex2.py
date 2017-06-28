import re


filename = "Big Bend.csv"

fout = open("output2.csv", "w")

regex = re.compile(r'<Object:<Path:/Databases/EGAPostBox/Rented/P[A-Z]+[0-9]+>,') 

with open(filename,'r') as f:
    next(f)
    for x in f:
        x = x.rstrip()
        if re.match(regex,x):            
            x = regex.sub("",x)
            fout.write(x+"\r\n")
        if not x:
            continue

# always close files
f.close()
fout.close()

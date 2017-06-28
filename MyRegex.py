import re
myregex = re.compile(r'<Object:<Path:/Databases/EGAPostBox/Rented/PO[0-9]+>,')
result = myregex.search("""<Object:<Path:/Databases/EGAPostBox/Rented/PO5023>,""")
print (result.group())

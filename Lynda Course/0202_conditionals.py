
#assign 0 to a and 1 to b
a,b = 0, 1

#assigns 2 to both c and d
c = d = 2

if a<b:
    print( ' a ({}) is less than b ({})'. format(a,b))
else:
    print( ' a ({}) is not less than b ({})'. format(a,b))

if a<b:
    print( ' a {} is less than b {}'. format(a,b))
else:
    print( ' a {} is not less than b {}'. format(a,b))

#some c like languages
#print(a<b ? "true" : "false")

print("true" if a<b else "false")

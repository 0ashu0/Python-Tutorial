#integers are immutable object
x = 42
x1 = id(x)
print(x1)

# variable x is referring to differen variable
x = 43
x2 = id(x)
print(x2)

#x1 and x2 are different

# we dont change the immutable value,
# we change the variable reference and made it refer to different object

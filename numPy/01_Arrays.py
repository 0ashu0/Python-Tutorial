#function shape?


import numpy as np

#create a rank 1 array
#type of below values are 'numpy.int32'
a = np.array([11,12,13])
print(type(a))
print(a.shape)
print(type(a[0]))
for i in a:
	print(i)

#creating a rank 2 array
b = np.array(
		[
			[11,23,33],
			[22,44,66]
		]
	)

print("shape of b", b.shape)
print(b[0,1], b[0,2], b[1,2], b[1])
#print whole column in np? ^


#changing shape exercise
shape1 = np.array(
	[
		[1,2,3],
		[4,5,6],
		[7,8,9],
		[10,11,12]
	]
	)

print(shape1.shape)

shape1.shape = (3,4)
print(shape1)

shape1.shape = (2,6)
print(shape1)
print()
#shape changing exercise done


#inbuilt functions in numpy
#fucntions for 0,1, and others
#values are 'numpy.float64' type

_zero = np.zeros(0)
print("np.zeros(0) ")
print("_zero ")
print(_zero)
print("_zero.shape ", _zero.shape)
print()

_zero = np.zeros(1)
print("np.zeros(1) ")
print("_zero ")
print(_zero)
print("_zero.shape ", _zero.shape)
print()

_zero = np.zeros(2)
print("np.zeros(2) ")
print("_zero ")
print(_zero)
print("_zero.shape ", _zero.shape)
print()

_zero = np.zeros((0))
print("np.zeros((0)) ")
print("_zero ")
print(_zero)
print("_zero.shape ", _zero.shape)
print()

_zero = np.zeros((1))
print("np.zeros((1)) ")
print("_zero ")
print(_zero)
print("_zero.shape ", _zero.shape)
print()

_zero = np.zeros((2))
print("np.zeros((2)) ")
print("_zero ")
print(_zero)
print("_zero.shape ", _zero.shape)
print()

_zero = np.zeros((0,0))
print("np.zeros((0,0)) ")
print("_zero ")
print(_zero)
print("_zero.shape ", _zero.shape)
print()

_zero = np.zeros((1,1))
print("np.zeros((1,1)) ")
print("_zero ")
print(_zero)
print("_zero.shape ", _zero.shape)
print()

_zero = np.zeros((2,2))
print("np.zeros((2,2)) ")
print("_zero ")
print(_zero)
print("_zero.shape ", _zero.shape)
print()

_zero = np.zeros((1,2))
print("np.zeros((1,2)) ")
print("_zero ")
print(_zero)
print("_zero.shape ", _zero.shape)
print()

_ones = np.ones(0)
print("np.ones(0) ")
print("_ones ")
print(_ones)
print("_ones.shape ", _ones.shape)
print()

_ones = np.ones(1)
print("np.ones(1) ")
print("_ones ")
print(_ones)
print("_ones.shape ", _ones.shape)
print()

_ones = np.ones(2)
print("np.ones(2) ")
print("_ones ")
print(_ones)
print("_ones.shape ", _ones.shape)
print()

_ones = np.ones((0))
print("np.ones((0)) ")
print("_ones ")
print(_ones)
print("_ones.shape ", _ones.shape)
print()

_ones = np.ones((1))
print("np.ones((1)) ")
print("_ones ")
print(_ones)
print("_ones.shape ", _ones.shape)
print()

_ones = np.ones((2))
print("np.ones((2)) ")
print("_ones ")
print(_ones)
print("_ones.shape ", _ones.shape)
print()

_ones = np.ones((0,0))
print("np.ones((0,0)) ")
print("_ones ")
print(_ones)
print("_ones.shape ", _ones.shape)
print()

_ones = np.ones((1,1))
print("np.ones((1,1)) ")
print("_ones ")
print(_ones)
print("_ones.shape ", _ones.shape)
print()

_ones = np.ones((2,2))
print("np.ones((2,2)) ")
print("_ones ")
print(_ones)
print("_ones.shape ", _ones.shape)
print()

_ones = np.ones((1,2))
print("np.ones((1,2)) ")
print("_ones ")
print(_ones)
print(type(_ones))
print(type(_ones[0,0]))
print("_ones.shape ", _ones.shape)
print()

_full = np.full((3,3), 7)
print("_full ")
print(_full)

_full = np.full((3,3), 7, 'int32')
print("_full ")
print(_full)

_random = np.random.random((2,2))
print(_random)
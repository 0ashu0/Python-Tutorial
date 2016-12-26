#http://cs231n.github.io/python-numpy-tutorial/#numpy
#http://www.python-course.eu/numpy.php

import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array(
	[
		[1,2,3,4],
		[5,6,7,8],
		[9,10,11,12]
	]
	)

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]

print(a[1:2])
print(a[1:3])

print(a[1])
print(a[:3])

print(a[:2])
print(a[1:3])

print(a[:0,:0])
print()
print(a[:0,:1])
print()
print(a[:0,:2])
print()
print(a[:0,:3])
print()
print(a[:1,:0])
print()
print(a[:2,:3])

print(a[1:2,2:3])
"""Bynary types: bytes, bytearray, memorytype."""


"""BYTES are the immutable version."""
bytes_str = bytes("Python is interesting.", 'utf-8')
print(bytes_str) #Printed: b'Python is interesting.' (Note: we have the letter b in front)

bytes_int = bytes(5)
print(bytes_int) #Printed: b'\x00\x00\x00\x00\x00'

bytes_list = bytes([1, 2, 3, 4, 5])
print(bytes_list) #Printed: b'\x01\x02\x03\x04\x05'


"""BYTEARRAY is the mutable version."""
bytearray_str = bytearray("Python is interesting.", 'utf-8')
print(bytearray_str) #Printed: bytearray(b'Python is interesting.)' (Note: we have the letter b in front)

bytearray_int = bytearray(5)
print(bytearray_int) #Printed: bytearray(b'\x00\x00\x00\x00\x00')

bytearray_list = bytearray([1, 2, 3, 4, 5])
print(bytearray_list) #Printed: bytearray(b'\x01\x02\x03\x04\x05')


"""MEMORYTYPE"""
"""
The memoryview() function returns a memory view object of the given argument. 
A memory view is a safe way to expose the buffer protocol in Python. 
It allows you to access the internal buffers of an object by creating a memory view object.
This memoryview() function takes a single parameter: obj - object whose internal data is to be exposed. 
Obj must support the buffer protocol (bytes, bytearray).
"""

"""
Why buffer protocol and memory views are important?
We need to remember that whenever we perform some action on an object (call a function of an object, slice an array), 
Python needs to create a copy of the object. If we have large data to work with (eg. binary data of an image), we would 
unnecessarily create copies of huge chunks of data, which serves almost no use.
Using the buffer protocol, which is only accessible to us at the C-API level and not using our normal codebase we can 
give another object access to use/modify the large data without copying it. This makes the program use less memory and 
increases the execution speed.
"""

#random bytearray
random_byte_array = bytearray('ABC', 'utf-8')

mv = memoryview(random_byte_array)

# access memory view's zeroth index
print(mv[0]) # Output: 65

# create byte from memory view
print(bytes(mv[0:2])) # Output: b'AB'

# create list from memory view
print(list(mv[0:3])) # Output: [65, 66, 67]

# update 1st index of mv to Z
mv[1] = 90
print('After updation:', random_byte_array) # Output: After updation: bytearray(b'AZC')
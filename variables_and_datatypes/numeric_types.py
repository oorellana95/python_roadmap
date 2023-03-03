"""Numeric Types:	int, float, complex"""


"""Integer types"""
"""
The following strings can be prepended to an integer value to indicate a base other than 10:
Prefix	                            Interpretation	                               Base
0b (zero + lowercase letter 'b')
0B (zero + uppercase letter 'B')	Binary	                                          2
0o (zero + lowercase letter 'o')
0O (zero + uppercase letter 'O')	Octal	                                          8
0x (zero + lowercase letter 'x')
0X (zero + uppercase letter 'X')	Hexadecimal	                                     16
"""
print(19) # Output: 19
print(0b10) # Output: 2
print(0o10) # Output: 8
print(0x10) # Output: 16


"""Floating point numbers"""
weight = 6.3
thickness = 1.
high = .3

"""Almost all platforms represent Python float values as 64-bit “double-precision” values, according to the IEEE 754 
standard. In that case, the maximum value a floating-point number can have is approximately 1.8 ⨉ 10308. Python will 
indicate a number greater than that by the string inf:"""
print(1.79e308) # Output: 1.79e+308
print(1.8e308) # Output: inf

"""The closest a nonzero number can be to zero is approximately 5.0 ⨉ 10-324. Anything closer to zero than that is 
effectively zero:"""
print(5e-324) # Output: 5e-324
print(1e-325) # Output: 0.0



"""Complex numbers"""
""" They are specified as <real part>+<imaginary part>j. For example:"""
complex_number = 2+3j # Output: (2+3j)

"""Kata for bitwise operators"""
print("Hello Bitwise Operators!")

a = 40
b = 15
print(a, bin(a), b, bin(b))

x = a & b 	# and
print(x, bin(x))

x = a | b	# or
print(x, bin(x))

x = a ^ b	# xor
print(x, bin(x))

x = ~a		# complement
print(x, bin(x))

x = a << 2	# left shift
print(x, bin(x))

x = a >> 2	# right shift
print(x, bin(x))


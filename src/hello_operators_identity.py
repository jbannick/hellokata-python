"""Kata for identity operators"""
print("Hello Identity Operators!")

a = 10
b = 10
print(a, id(a), b, id(b))

print(a is b)
print(id(a) == id(b))

c = 10 / 2
d = 20 / 4
print(c is d)
print(id(c) == id(d))

print(a is c)
print(id(a) == id(c))

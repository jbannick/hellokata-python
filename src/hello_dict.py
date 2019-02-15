"""Kata for dictionaries"""
print("Hello Dictionaries!")

mydict = {}
mydict['one'] = "This is one"
mydict[2] = "This is two"

tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}

print(mydict['one'])       # Prints value for 'one' key
print(mydict[2])           # Prints value for 2 key
print(tinydict)            # Prints complete dictionary
print(tinydict.keys())     # Prints all the keys
print(tinydict.values())   # Prints all the values

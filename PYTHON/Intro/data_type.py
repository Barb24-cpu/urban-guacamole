# Example variables
x = 10         # Integer
y = 3.14       # Float
z = "Hello"    # String
a = True       # Boolean<True, False>
b = [1, 2, 3, 4] # List <Array> Mutable <By value>
c = {1, 2, 3}  # Set
d = (1, 2, 3)  # Tuple <List> Immutable
e = {"key": "value"}
# Dictionary <Object:js>
# for dictionary use Bracket notation

# Determining the types
#`y is ${}`
print("X is ",x,"Its type ",type(x)) # Output: <class 'int'>
print(f"Y is {y} its type is {type(y)}") # Output: <class 'float'>
print(type(z)) # Output: <class 'str'>
print(type(a)) # Output: <class 'bool'>
print(type(b)) # Output: <class 'list'>
print(type(c)) # Output: <class 'set'>
print(type(d)) # Output: <class 'tuple'>
print(type(e)) # Output: <class 'dict'>
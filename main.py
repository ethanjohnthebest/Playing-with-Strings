# 1. print function and type conversion

a = float(1)
b = int(5.5)
c = complex(1)


print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

"""
1.0
5
(1+0j)

<class 'float'>
<class 'int'>
<class 'complex'>
"""

# 2. string operations

# A. Concatenation

firstname = "Ethan"
Lastname = "John"
fullname = firstname +" "+ Lastname
print(fullname)

# B. Repetion
card = "EJK"
print(card * 3)

# C. Slicing
# Give the chareter from the index(staing from 0)

firstname = "Elaine"
Lastname = "Richa"
print(firstname[3])
print(Lastname[0])
print(firstname[1])

# D. Rage Slice
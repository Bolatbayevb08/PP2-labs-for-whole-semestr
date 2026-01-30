#1 example integer
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
#2 example complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
#3 example random number
import random

print(random.randrange(1, 10))
#4 example division
print(10 / 2)  # float
print(10 // 2) # int

#5 example
x = 2    
y = 10.8  
z = 3j   
#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
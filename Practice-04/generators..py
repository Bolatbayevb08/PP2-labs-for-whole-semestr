# 1. Generator that generates squares up to N
def squares_upto_n(n):
    for i in range(n + 1):
        yield i * i

print("Squares up to 5:")
for num in squares_upto_n(5):
    print(num)


# 2. Even numbers between 0 and n (comma separated)
n = int(input("Enter n: "))

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

print(",".join(str(num) for num in even_numbers(n)))


# 3. Numbers divisible by 3 and 4 between 0 and n
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("Divisible by 3 and 4:")
for num in divisible_by_3_and_4(50):
    print(num)


# 4. Generator squares from a to b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

print("Squares from 2 to 6:")
for value in squares(2, 6):
    print(value)


# 5. Generator from n down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

print("Countdown from 5:")
for num in countdown(5):
    print(num)
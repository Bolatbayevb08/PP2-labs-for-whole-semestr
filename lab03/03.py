digit_map = {
    "ZER": "0",
    "ONE": "1",
    "TWO": "2",
    "THR": "3",
    "FOU": "4",
    "FIV": "5",
    "SIX": "6",
    "SEV": "7",
    "EIG": "8",
    "NIN": "9"
}

reverse_map = {v: k for k, v in digit_map.items()}


def decode(s):
    number = ""
    for i in range(0, len(s), 3):
        triplet = s[i:i+3]
        number += digit_map[triplet]
    return int(number)


def encode(num):
    if num == 0:
        return "ZER"
    
    result = ""
    for digit in str(num):
        result += reverse_map[digit]
    return result


expression = input()


for op in "+-*":
    if op in expression:
        operator = op
        break

left, right = expression.split(operator)

num1 = decode(left)
num2 = decode(right)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
else:
    result = num1 * num2

print(encode(result))

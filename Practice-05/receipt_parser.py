import re

with open("raw.txt", "r") as file:
    data = file.read()

print("----- Receipt Data -----")
print(data)


# Prices
prices = re.findall(r"\d+\.\d{2}", data)
print("\nPrices:", prices)


# Product names
products = re.findall(r"[A-Za-z]+\s+\d+\.\d{2}", data)
product_names = [p.split()[0] for p in products]
print("\nProducts:", product_names)


# Total amount
total = re.search(r"Total:\s*(\d+\.\d{2})", data)
if total:
    print("\nTotal:", total.group(1))


# Date
date = re.search(r"\d{4}-\d{2}-\d{2}", data)
if date:
    print("\nDate:", date.group())


# Time
time = re.search(r"\d{2}:\d{2}", data)
if time:
    print("\nTime:", time.group())


# Payment Method
payment = re.search(r"Payment Method:\s*(\w+)", data)
if payment:
    print("\nPayment Method:", payment.group(1))
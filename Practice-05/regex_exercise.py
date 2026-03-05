import re

print("----- 1. 'a' followed by zero or more 'b' -----")

pattern = r"ab*"
strings = ["a", "ab", "abb", "abbb", "ac"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(s, "-> Match")
    else:
        print(s, "-> No match")


print("\n----- 2. 'a' followed by 2-3 'b' -----")

pattern = r"ab{2,3}"
strings = ["ab", "abb", "abbb", "abbbb"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(s, "-> Match")


print("\n----- 3. Lowercase words joined with underscore -----")

text = "hello_world test_case python_program"
pattern = r"[a-z]+_[a-z]+"

matches = re.findall(pattern, text)
print(matches)


print("\n----- 4. Uppercase followed by lowercase -----")

text = "Hello World Python Regex Example"
pattern = r"[A-Z][a-z]+"

print(re.findall(pattern, text))


print("\n----- 5. 'a' followed by anything ending with 'b' -----")

pattern = r"a.*b"
strings = ["ab", "acb", "axyzb", "a123b"]

for s in strings:
    if re.fullmatch(pattern, s):
        print(s, "-> Match")


print("\n----- 6. Replace space, comma, dot with colon -----")

text = "Hello, world. Python is great"

result = re.sub(r"[ ,\.]", ":", text)
print(result)


print("\n----- 7. snake_case to camelCase -----")

def snake_to_camel(text):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)

print(snake_to_camel("hello_world_python"))


print("\n----- 8. Split string at uppercase letters -----")

text = "HelloWorldPythonRegex"

result = re.split(r"(?=[A-Z])", text)
print(result)


print("\n----- 9. Insert spaces before capital letters -----")

text = "HelloWorldPython"

result = re.sub(r"([A-Z])", r" \1", text).strip()
print(result)


print("\n----- 10. camelCase to snake_case -----")

def camel_to_snake(text):
    return re.sub(r"([A-Z])", r"_\1", text).lower()

print(camel_to_snake("helloWorldPython"))


print("\n----- Examples of regex functions -----")

text = "Python is powerful"

# search
match = re.search("power", text)
print("search:", match.group())

# match
match = re.match("Python", text)
print("match:", match.group())


print("\n----- Special sequences examples -----")

text = "User123 logged in at 10:45"

print("Digits:", re.findall(r"\d+", text))
print("Words:", re.findall(r"\w+", text))
print("Spaces:", re.findall(r"\s", text))
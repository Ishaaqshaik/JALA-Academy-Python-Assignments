# Different ways creating a string

str6 = 'Hello World'
print(str6)

string = "JALA"
print(string)

string1 = '''Python'''
print(string1)

string2 = """I am Ishaaq shaik """ 
print(string2)
print()

# Concatenating two strings using + operator 

Str122 = string + string1 
print("Concatenating two strings :  ", Str122)
print()

# Finding the length of the string 

stringg = "i am ishaaq shaik"
print("finding the length ",len(stringg))
print()

#  Extract a string using Substring

str = "Python Programming"
substring = str[0:6]
print(substring)

# Searching in strings using index() 

str0 = "HELLO WORLD "
str1 = "RLD"
print("Finding the index : ",str0.index(str1))
print()


# Matching a String Against a Regular Expression With matches() 

import re

text = "HELLO123"

pattern = r"^[A-Za-z0-9]+$"  # Only letters and numbers

result = re.fullmatch(pattern, text)

if result:
    print("Match Found: True")
else:
    print("Match Found: False")
print()


# Comparing strings

txt1 = "ishaaq"
txt2 = "shaik"
txt3 = "hello"
txt11 = txt1
print(txt1 == txt2)
print(txt2 == txt3)
print(txt3 != txt1 )
print(txt1 == txt11)
print()

# startsWith(), endsWith() and compareTo() 

string = 'Ishaaq Shaik'
print(string.startswith("Ishaaq "))
print(string.endswith("Shaik"))
print()

# Trimming strings with strip().

txt = 'Hello World welcome'
print(txt.strip("world"))
print()

# Replacing characters in strings with replace()
string = 'bye World'
print(string.replace("bye","Hello"))
print()

# Splitting strings with split()

str9 = 'hi-hello-bye'
print(str9.split("-"))
print()

# Converting integer objects to Strings.

str = "10"
number1 = int(str)
print(number1)
print(type(number1))
print()

# Converting to uppercase and lowercase.
txt = 'hello'
txt1 = 'WORLD'
print(txt.upper())
print(txt1.lower())
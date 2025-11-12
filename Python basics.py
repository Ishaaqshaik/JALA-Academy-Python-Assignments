#Write a program to print your name.

print("Ishaaq")

#Write a program for a Single line comment and multi-line comments


print(" multi-line comments.")


#Define variables for different Data Types int, Boolean, char, float, double and print on the Console.


a = 50
print("Type of a: ", type(a))
b = False
print("Type of b: ", type(b))
c = 5.0
print("Type of c: ", type(c))
String = 'Hello'
print("Type of String: ", type(String))


#Define the local and Global variables with the same name and print both variables and understand the scope of the variables

a = 5 #global

def display_mess():
    # Local variable 
    m = 7
    print("Inside the function:", m)

# Function call
display_mess()

# Printing the global variable
print("Outside the function:", a)

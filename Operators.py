#Write a function for arithmetic operators(+,-,*,/)

def operations(a, b):
    print("Add:", a + b)
    print("Sub:", a - b)
    print("Multi:", a * b)
    print("Div:", a / b)


operations(10, 5)


# Write a method for increment and decrement operators(++, --)


I = 0
I += 1
I = I+1
print('The value of a is ',I)
#increment
print("INCREMENTED FOR LOOP")
for i in range(0, 5):
   print(i)
#decrement
print("\nDECREMENTED FOR LOOP")
for i in range(4, -1, -1):
   print(i)




#Write a program to find the two numbers equal or not.

a = int(input("enter the number : "))
b = int(input("enter the number: "))
if a == b:
    print("yes both are equal")
else:
    print("not equal")





#Program for relational operators (<,<==, >, >==)


a = 10
b = 15
print(a < b)  
print(a <= b) 
print(a > b)  
print(a >= b)  
print(a == b) 
print(a != b)



#Print the smaller and larger number


a = 10
b = 15

if a > b:
    print("Greater ", a)
else:
    print("Smaller", b)



























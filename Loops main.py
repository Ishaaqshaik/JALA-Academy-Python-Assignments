# Write a program to print  “Bright IT Career”  ten times using for loop 

i= 1
while i <= 10:
    print("Bright IT Career")

    i = i+1


# Write a python program to print 1 to 20 numbers using the while loop.

i = 0
while i<=20:
    print(i)

    i = i+1


#Program to equal operator and not equal operators 

a =10
b = 15

print(a==b)
print(a !=b)


# Write a program to print the odd and even numbers. 


N = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("Even Numbers: ")  
for i in N:     
    if i%2==0:       
        print(i, end =" ")    
print("\nOdd Numbers:")
for i in N:
    if i%2!= 0:
        print(i, end =" ")
print()

#Write a program to print largest number among three numbers. 

a = 30
b = 20
c = 25

if a > b and a > c:
    largest = a 
elif b > c and b > c:
    largest = b
else:
    largest = c

print("largest is ", largest)


#Write a  program to print even number between 10 and 20 using while 

i=10
while i<=20:
    if i%2== 0:
        print("even", i)
    i=i+1

# Write a program to print 1 to 10 using the do-while loop statement. 

a = 1
print(end=" ")
while True:
    print(a,end=" ")
    a = a + 1
    if(a > 10):
        break 


#Write a program to find Armstrong number or not 

a = 153
sum = 0
temp = 0
temp = a
while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10
if a == sum:
    print(a," is an amstrong number")
else:
    print(a," is not an amstrong number")


# Write a program to find the prime or not. 

num = 11 

if num > 1:
    d=2
    while d <= num//2:
        if num%2 == 0:
            break
        else:
            print("yes its prime",num)
            break



#. Write a program to palindrome or not. 

num = 150
rev = 0
bkp = num 
while num > 0:
    t = num % 10
    rev = rev*10+t
    num = num //10

if bkp == rev:
    print("yes it's a palindrom" )
else:
    print("not a plaindrom")




#Program to check whether a number is EVEN or ODD using switch 

num = 10

if num %2 == 0:
    print("even")
else:
    print("odd")


#Print gender (Male/Female) program according to given M/F using switch

cha = input("Enter M or F: ")

match cha.upper():
    case "M":
        print("Male")
    case "F":
        print("Female")
    case _:
        print("Invalid Input")


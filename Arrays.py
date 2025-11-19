#Write a function to add integer values of an array 

def array(arr):
    total = 0
    for num in arr:
        total += num
    return total

nums = [10, 20, 30, 40, 50]
print("Sum =", array(nums))

# Write a function to calculate the average value of an array of integers 

def cal(arr):
    total = 0 
    for num in arr:
         total = total + num 
         avg = total / len(arr)
    return avg
 
    
nums = [1,2,3,4,5]
print("Avg= ", cal(nums))


# Write a program to find the index of an array element 

arr = [1,3,5,2,6,7,9,8]

index = arr.index(5)
print(index)

index = arr.index(7)
print(index)


# Write a function to test if array contains a specific value 

arr = [125,115,125,145,1,175]

for i in arr:
    if i == 1:
        print("yes it exites")
    else:
        print("no it not exites")


arr = [10,2,30,40,50,60]

for i in arr:
    if i == 2:
        arr.remove(2)
print(arr)

# Write a function to copy an array to another array 

arr1 = [1,2,3,4,6,5]
arr2 = []
for i in arr1:
    arr2.append(i)
print(arr2)

# Write a function to insert an element at a specific position in the array

arr = [1,2,3,4,5,6,9,8,7]
arr.insert(1,0) 
print(arr)

# Write a function to find the minimum and maximum value of an array.

arr = [100,35000,7000,20,50,9000,100,103]
minposition = arr.index(min(arr))
print ("The min position:", minposition)

maxposition = arr.index(max(arr))
print ("The max position::", maxposition)

 # Write a function to find the duplicate values of an array.
   
arr = [21,11,31,13,11]
for i in range(0,len(arr)):
    for k in range(i + 1,len(arr)):
        if arr[i] == arr[k]:
            print("Duplicate element in array:",arr[k])


# Write a program to find the common values between two arrays.


arr = ['i','s','h','a','a','q']
arr1 = ['s','h','q']
print("Common values in given arrays:",set(arr).intersection(arr1))


# Write a method to remove duplicate elements from an array.


arr = [10,20,30,45,10,85]
final_arr = [] 
for i in arr:
    if i not in final_arr:
        final_arr.append(i)
print(final_arr)

# Write a method to find the second largest number in an array.


arr = [10,40,22,75,60,50,800,300,900]
arr.sort()  
print("Second largest number:",arr[-2]) 


# Write a method to find number of even number and odd numbers in an array.


arr = [1,2,3,4,5,6,7,8,9]
evennum = 0
oddnum = 0
for i in arr:
    if i % 2 == 0:
        evennum += 1
    else:
        oddnum += 1 
print("Even Numbers in given array:",evennum)
print("Odd Numbers in given array:",oddnum)

# Write a function to get the difference of largest and smallest value.

arr = [10,6,11,13,14]
arr.sort() 
print("Diffrence of largest and smallest value:",arr[4]-arr[0])

# Write a method to verify if the array contains two specified elements(12,23).

arr = [1,10,17,12,16,23]
for i in arr:
    if i == 17:
        print("Exist in array")
    if i == 23:
        print("Exist in array")


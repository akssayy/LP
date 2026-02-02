"""2. Moderate–Hard
Given a list of integers:
nums = [4, 7, 2, 7, 9, 2, 4, 10] 
Write a program to:
Remove duplicate elements without using set
Sort the list in ascending order
Print the second largest number 2, 4, 7, 9, 10"""

nums = [4, 7, 2, 7, 9, 2, 4, 10]
num1 = []

for i in nums:
    if i not in num1:
        num1.append(i)
        print(num1) 

num2  = sorted(num1)




    

    
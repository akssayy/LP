"""Given two lists:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
Write a program to:
Find common elements using a loop
Find elements present only in list1
Find elements present in either list but not both
(Do not use set operations directly)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list3 = []

for i in list1:
    if i not in list2:
         list3.append(i)

for x in list2:
     if x not in list1:
          list3.append(x)
            

print(list3)
"""

"""numbers = [ 2, 4, 6, 8]
new_list = []

for number in numbers:
     new = number + number
     new_list.append(new)

print(new_list)"""


numbers = [6, 7, 8, 9, 10]

def count_even(numbers):
     count = 0
     for number in numbers:
          if number % 2 == 0:
               count += 1
                 
     return count 


print(count_even(numbers))



    
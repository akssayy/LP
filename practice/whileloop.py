""""1️ Print numbers from 10 to 1
Output: 10 9 8 7 ... 1"""

"""
i = 10
while i >= 1:
    print(i)
    i -= 1
"""

"""
(2)
Print all even numbers between 1 and 50
"""
"""
i = 2
while i <= 50:
    print(i)
    i += 2
"""
"""
3️⃣ Sum of first N natural numbers

Input: N = 5
Output: 15
"""
"""
num = int(input("enter a number: "))
i = 1 
total = 0 

while i <= num:
    total = i + total
    i += 1

print(f"sum is {total}")

"""

num = int(input("enter a number"))

for i in range(1,11):
    print(i * num)
"""num = {1, 2, 5, 2, 4, 1}
num.add(7)
num.remove(5)
print(num)
if 4 in num:
    print("found")"""

set = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set.difference(set2)
print(f"{set3}")

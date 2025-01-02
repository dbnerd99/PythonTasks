"""
Task 3
Find the second largest number in a list.
Input: [10, 20, 4, 45, 99]
Output: 45
"""

List_1 = []
numbers = int(input("How many numbers do you wanna add to the list? "))
for i in range(0, numbers):
    numbers_to_add = int(input("Numbers to be added "))
    List_1.append(numbers_to_add)

print(List_1)

List_1.sort()
print(f"the second largest number is {List_1[-2]}")

"""
Output : 
How many numbers do you wanna add to the list? 5
Numbers to be added 10
Numbers to be added 20
Numbers to be added 4
Numbers to be added 45
Numbers to be added 99
[10, 20, 4, 45, 99]
the second largest number is 45

Process finished with exit code 0
"""
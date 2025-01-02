string_1 = input("Enter a number ")

if string_1.isdigit():
    number = int(string_1)
    print(f"you entered: {number}")
else:
    print("Invalid input. Please enter a number.")

"""
Output 1 :
Enter a number 123
you entered: 123

Process finished with exit code 0

Output 2 :
Enter a number abc
Invalid input. Please enter a number.

Process finished with exit code 0
"""
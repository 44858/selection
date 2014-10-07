#Lewis Travers
#07/10/2014
#Grading an exam mark

mark = int(input("Please enter the number of marks out of 100: "))

if mark >= 81:
    print("A Grade")
elif mark >= 71:
    print("B Grade")
elif mark >= 61:
    print("C Grade")
elif mark >= 51:
    print("D Grade")
elif mark >= 41:
    print("E Grade")
else:
    print("U Grade")

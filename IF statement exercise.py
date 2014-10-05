#Lewis Travers
#25/09/2014
#IF statement exercise

user_age = int(input("Please enter your age: "))
if user_age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")

retire = 65 - user_age

print("You will be able to retire in {0} years.".format(retire))

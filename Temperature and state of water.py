#Lewis Travers
#03/10/2014
#Temperature and state of water

temperature = int(input("Please enter the temperature of the water: "))

if temperature > 100:
    print("The water is boiling")
elif temperature > 0:
    print("The water is not boiling nor is it frozen")
elif temperature < 0:
    print("The water is frozen")

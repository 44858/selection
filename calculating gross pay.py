#Lewis Travers
#03/10/2014
#Calculating gross pay

hours = int(input("Please enter the number of hours worked this week: "))

hourly_pay = int(input("Please enter your hourly pay: "))

overtime_pay = hourly_pay * 1.5

total_pay = hours * overtime_pay

gross_pay = hours * hourly_pay

if hours >60 or hours <0:
    print("That is not a valid amount of hours.")
if hours >= 40:
    print("Your total pay is £{0}".format(total_pay))
else:
    print("Your total pay is £{0}".format(gross_pay))

    

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
# Tip: There are 2 ways to round a number

print("Welcome to the tip calculator")
bill = float(input("What was your total bill?\n $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
person = int(input("How many people to split the bill?\n"))

act_tip = tip/100
new_tip= bill*act_tip
act_bill= new_tip+bill
pay = act_bill/person
rounded_pay = "{:.2f}".format(pay)

print(f"Each person should pay: ${rounded_pay}")
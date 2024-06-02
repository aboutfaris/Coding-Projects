#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Text Front-End
print("Welcome to the tip calculator!")
bill = int(input("What was the bill?"))
tip =  float(input("How much would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

# Back-End
tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
bill_per_people = total_bill / people
final_bill = round(bill_per_people, 2)
final_bill = "{:.2f}".format(bill_per_people)

#Results
print(f"Each person should pay: ${final_bill}")






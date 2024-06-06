# Love Calculator

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combinednames = name1 + name2
lowernames = combinednames.lower()
t = lowernames.count("t")
r = lowernames.count("r")
u = lowernames.count("u")
e = lowernames.count("e")
firstdigit = t + r + u + e
l = lowernames.count("l")
o = lowernames.count("o")
v = lowernames.count("v")
e = lowernames.count("e")
seconddigit = l + o + v + e

Lovescore = int(str(firstdigit) + str(seconddigit))
z = Lovescore
# Conditions
if z < 10 or z > 90:
  print(f"Your score is {z}, you go together like coke and mentos.")
elif z >= 40 and z <= 50:
  print(f"Your score is {z}, you are alright together.")
else:
  print(f"Your score is {z}.")

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# output is like
# You have {days} days, {weeks} weeks, and {months} months left.

# given premises is:
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

years_left = 90 - int(age)
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
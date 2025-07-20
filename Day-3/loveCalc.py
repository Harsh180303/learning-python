# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

combined_names = name1 + name2
# print(combined_names)

t_occurs = combined_names.count('t')
r_occurs = combined_names.count('r')
u_occurs = combined_names.count('u')
e_occurs = combined_names.count('e')

total1 = t_occurs + r_occurs + u_occurs + e_occurs

l_occurs = combined_names.count('l')
o_occurs = combined_names.count('o')
v_occurs = combined_names.count('v')
e_occurs = combined_names.count('e')

total2 = l_occurs + o_occurs + v_occurs + e_occurs

love_score = total1 * 10 + total2

if love_score < 10 or love_score > 90 :
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50 :
    print(f"Your score is {love_score}, your are alright together.")
else :
    print(f"Your socre is {love_score}")
num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("Your name is " + new_num_char + " characters long.")

# Better way
num_char = len(input("What is your name?\n"))
print("Your name has", num_char, "Characters")

# MORE 

a = float(234345)
print(type(a))
print(a)

# Implicit Type Conversion (a.k.a. Type Coercion)
print(70 + float("100.5"))
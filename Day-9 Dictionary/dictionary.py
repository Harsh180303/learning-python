programming_dictionary = {
    "Bug": "An error in a prgram that prevents the program form running as expected.",
    "Function": "A piece of code that can easily call over and over again."
}

# Retrieving items from dictionary.
print(programming_dictionary["Bug"])

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "It is simpally an error in programming language."
print("See this: ",programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

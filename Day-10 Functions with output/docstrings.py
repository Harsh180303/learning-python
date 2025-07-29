# Docsting is used to create a documentaion of our own function so that we can understand the behaviour of our fuction while using it. It always written just below the function declaration line. It enclosed with three double quotes --- ["""This is the docstring"""]

def format_name(f_name, l_name):
    """Take a first and last name and format
    it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "Invalid input"
    full_name = f"{f_name} {l_name}"
    return full_name.title()

first_name = input("What is you first name?: ")
last_name = input("What is you last name?: ")
format_name(f_name=first_name, l_name=last_name)
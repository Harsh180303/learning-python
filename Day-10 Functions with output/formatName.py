def formated_name(f_name, l_name) :
    if f_name == '' or l_name == '':
        return "Please provide a valid input"
    full_name = f"{f_name} {l_name}"
    return full_name.title()
    
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(formated_name(f_name=first_name, l_name=last_name))
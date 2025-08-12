from resources_and_menu import resources, MENU

def showReport() :
    curr_report = {}
    for item in resources:
        curr_report[item] = resources[item]
    return curr_report


def is_resources_sufficient(type_of_drink) :
    # water = MENU[type_of_drink]['ingredients']['water']
    # milk = MENU[type_of_drink]['ingredients']['milk']
    # coffee = MENU[type_of_drink]['ingredients']['coffee']

    for ingredients in MENU[type_of_drink]["ingredients"]:
        print(MENU[type_of_drink]["ingredients"][ingredients])


drink = input("What would you like? (Espresso/ Latte/ Cappuccino): ").lower()
if drink == "report":
    report = showReport()
    for item in resources:
        print(f"{item} : {resources[item]}")

if drink == "latte":
    if is_resources_sufficient(drink):
        print("this")

is_resources_sufficient("latte")
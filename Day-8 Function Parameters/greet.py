def greet() :
    name = input("What is your name? ")
    ask = input(f"Hi {name}, how are you? ")
    print(f"Okay {name}, I'm actually getting late. Let's catch up later.")

# greet()

def greet_with_perams(name) :
    print(f"Hi {name}")
    print(f"Okay {name}, I'm getting late. could u please drop me there")

# greet_with_perams(name="Harsh")


def greet3(name, location) :
    print(f"Hi {name},")
    print(f"What do you like in {location}")

# Positional argument
# greet3("Harsh", "Bhopal")

# keyword argument
# greet3(name="Harsh", location="Bhopal")


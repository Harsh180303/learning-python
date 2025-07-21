states_of_india = ["mp", "up", "delhi", "mumbai",]
print(states_of_india)
states_of_india.extend(['goa', "rajasthan", "haryana", "gujrat"])
print(states_of_india)

states_of_india.insert(2, "ukd")
print("after inserting : ", states_of_india)

states_of_india.remove("goa")
print("after removing", states_of_india)
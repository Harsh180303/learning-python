import math

def paint_calc(height, width, coverage):
    no_of_cans = math.ceil(float(height * width) / int(coverage))
    print(f"You'll need {no_of_cans} cans of paint")

wall_h = float(input("Height of wall (in ft): "))

wall_w = float(input("Width of wall (in ft): "))

coverage = 5 # coverage of can is 5 sqft

paint_calc(wall_h, wall_w, coverage)
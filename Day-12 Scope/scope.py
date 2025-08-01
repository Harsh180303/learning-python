# Example

enemies = 1

def increase_enemies() :
    enemies = 2
    print(f"Enemies insied function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")
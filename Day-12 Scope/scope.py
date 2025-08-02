# Example


# In this way you can access enemies which is outside the function but not recommended
enemies = 1

def increase_enemies() :
    global enemies
    print(f"Enemies insied function before increasing: {enemies}")
    enemies += 1
    print(f"Enemies insied function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")


# Instead of doing this (above) you can return the modifies value

enemies = 1

def increase_enemies() :
    print(f"Enemies insied function before increasing: {enemies}")
    return enemies + 1
    # print(f"Enemies insied function: {enemies}")

enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")
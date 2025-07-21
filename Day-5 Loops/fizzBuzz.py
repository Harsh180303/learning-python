# if number is fully devisible by 3 print Fizz
# if number is fully devisible by 5 print Buzz
# if number is fully devisible by 3 and 5 both print FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else :
        print(number)
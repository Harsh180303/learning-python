alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def caesar(cipher_direction, start_text, shift_amount) :
    end_text = ""
    
    if cipher_direction == "decode" :
        shift_amount *= -1
        
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    
    print(f"Your {cipher_direction}d value is: {end_text}")

from art import logo
print(logo)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(direction, text, shift)

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
    if choice == 'no':
        should_continue = False
        print("Goodbye.")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount) :
    cipher_text = ''
    for letter in plain_text:
        positon = alphabet.index(letter)
        new_position = positon + shift_amount
        cipher_text += alphabet[new_position]
    print(f"Your encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ''
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"Your decoded text is {plain_text}")

    
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode".lower() :
    encrypt(text, shift)
elif direction == "decode".lower() :
    decrypt(text, shift)
else :
    print("Please choose among encode or decode only nothing else.")
    
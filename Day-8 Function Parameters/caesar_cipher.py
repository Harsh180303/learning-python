alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
def caesar(cipher_direction, start_text, shift_amount) :
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "encode".lower() :
            new_position = position + shift_amount
        elif cipher_direction == "decode".lower() :
            new_position = position - shift_amount
    
        end_text += alphabet[new_position]
    
    print(end_text)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(direction, text, shift)
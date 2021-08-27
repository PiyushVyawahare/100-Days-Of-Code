alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    s = ""
    for letter in text:
        new_pos = alphabet.index(letter)+shift
        if new_pos>25:
            new_pos = new_pos-26
        s += alphabet[new_pos]
    print(f"The encoded text is : {s}")

encrypt(text, shift)
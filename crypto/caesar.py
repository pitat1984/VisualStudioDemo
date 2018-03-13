from helpers import alphabet_position, rotate_character
    
def encrypt(text,rot):

    encrypted_word = ""

    for char in text:
        letter = rotate_character(char,rot)
        encrypted_word = encrypted_word + letter
    return encrypted_word

def main():
    text = input("Type a message: ")
    num = int(input("Rotate by: "))
    print(encrypt(text,num))

if __name__ == '__main__':
    main()
from helpers import alphabet_position, rotate_character

    
def encrypt(text,key):

    encrypted_word = ""
    rot = 0
    i = 0

    for char in text:
        if char.isalpha() == True:
            rot = alphabet_position(key[i])
            letter = rotate_character(char,rot)
            encrypted_word = encrypted_word + letter
            i = i + 1
            if i == len(key):
                i = 0
        else:
            encrypted_word = encrypted_word + char
    return encrypted_word

def main():
    text = input("Type a message: ")
    key = input("Encryption key: ")
    print(encrypt(text,key))

if __name__ == '__main__':
    main()
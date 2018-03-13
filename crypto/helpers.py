def alphabet_position(letter):

    s = letter.lower()
    position = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in alphabet:
        if s == i:
            break
        position = position + 1
    return position

def rotate_character(char,rot):
    position = alphabet_position(char)
    i = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_up = alphabet.upper()

    if char in alphabet:
        
        while i < rot:
            i = i + 1
            position = position + 1
            if position == 26:
                position = 0
        return alphabet[position]

    elif char in alphabet_up:
        while i < rot:
            i = i + 1
            position = position + 1
            if position == 26:
                position = 0
        return alphabet_up[position]
    else:
        return char
def get_initials(fullname):
    index = 0
    space = " "
    name = ""
    initials = fullname[0]
    initial = ""

    for each_char in fullname:

        if each_char == space:
            initials = initials + fullname[index+1]
        index = index + 1      
        
    return initials.upper()

def main():
    person = input('What is your name? ')
    print(get_initials(person))

if __name__ == '__main__':
    main()

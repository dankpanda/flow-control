# Number 4
def vowel_check():
    vowel = ["a", "i", "u", "e", "o"]
    letter_input = input("Input a letter: ")
    if type(letter_input) == str:
        if len(letter_input) == 1:
            if letter_input in vowel:  
                print("It is a vowel")
            else:
                print("It is not a vowel")
        else:
             print("Only 1 character is allowed")
    else:
        print("Not a string")
    
vowel_check()

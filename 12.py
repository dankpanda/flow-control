def pig_latin():
    text:str = input("Enter your text: ")
    return text[1:len(text):] + text[0:1:] + "ay"

print(pig_latin())
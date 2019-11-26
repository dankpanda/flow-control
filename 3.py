def length():
    text = input("Enter your text: ")
    length = 0
    for i in text:
        length +=1
    return length
print(length())
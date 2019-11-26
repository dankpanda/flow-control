def palindrome():
    text = input("Enter your phrase: ")
    text_no_space = text.replace(" ", "")
    if text_no_space.lower() == text_no_space[::-1].lower():
        return "It is a palindrome"
    return "It is not a palindrome"

print(palindrome())
    
    

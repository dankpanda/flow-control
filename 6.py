# Number 6
def is_palindrome():
    text = input("Enter your text: ")
    return text[::-1]==text
    
print(is_palindrome())
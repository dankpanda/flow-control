def generate_n_chars(n:int, c:str):
    text = ""
    for i in range(n):
        text += c
    return text

print(generate_n_chars(5,"X"))
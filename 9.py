def get_score():
    score = float(input("Enter score: "))
    if score > 1:
        return "Error, score cannot be more than 1.0"
    elif score == 1 or score >= 0.9:
        return "A"
    elif score < 0.9 and score >= 0.8:
        return "B"
    elif score < 0.8 and score >= 0.7:
        return "C"
    elif score < 0.7 and score >= 0.6:
        return "D"
    return "F"

print(get_score())
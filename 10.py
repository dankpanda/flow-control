def calculate_pay():
    hours_value = int(input("Enter hours: "))
    rate_value = int(input("Rate: "))
    if hours_value > 40:
        pay_value = (40 * rate_value) + ((hours_value - 40) * (rate_value * 1.5))
    else:
        pay_value = hours_value * rate_value
    return pay_value

print(calculate_pay())
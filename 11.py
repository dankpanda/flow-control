def distance_from_zero(value):
    if type(value) == str:
        return "Nope"
    if value < 0:
        return value * -1
    return value

print (distance_from_zero("what?"))
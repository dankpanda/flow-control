def max_of_three(x:float,y:float,z:float):
    if x>y and x>z:
        return x
    if y>z and y>x:
        return y
    return z

print(max_of_three(3,4,2))
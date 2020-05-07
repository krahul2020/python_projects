weight=int(input('Enter your weight: '))
unit=input("(l)bs or '(k)gs: ")
if unit=="l"or"L":
    print(f"You are {weight*0.45} kgs")
elif unit=="k" or "K":
    print(f"You are   {weight/0.45}  lbs")
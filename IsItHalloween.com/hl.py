month, day = input().split()
if (month == 'OCT' and int(day) == 31) or (month == 'DEC' and int(day) == 25):
    print("yup")
else:
    print("nope")
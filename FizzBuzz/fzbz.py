x, y, n = input().split()
x = int(x)
y = int(y)
n = int(n)

for i in range(n):
    if (i+1) % x == 0:
        if (i+1) % y == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif (i+1) % y == 0:
        print("Buzz")
    else:
        print(str(i+1))
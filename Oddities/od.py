rep = int(input())
for _ in range(rep):
    aux = int(input())
    if aux % 2 == 0:
        print(f"{aux} is even")
    else:
        print(f"{aux} is odd")
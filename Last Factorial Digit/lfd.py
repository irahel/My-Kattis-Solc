rep = int(input())
for i in range(rep):
    aux = int(input())
    fat = 1
    while (aux > 0):
        fat = fat * aux
        aux -= 1    
    print(str(fat)[len(str(fat))-1])
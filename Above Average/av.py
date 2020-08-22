def med(l, num):
    suma = 0
    for i in range(len(l)):
        suma += int(l[i])
    return float(suma/int(num))
        

rep = int(input())
for _ in range (rep):
    total_sum = 0
    line = input()
    l = line.split()
    medium = med(l[1:], l[0])
    for i in range(len(l[1:])):
        if float(l[i+1]) > medium:
            total_sum+=1

    total_sum = (total_sum/int(l[0]))*100
    print('%.3f' %total_sum, end='%\n')
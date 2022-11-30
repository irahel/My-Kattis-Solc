def med(l, num):
    suma = sum(int(l[i]) for i in range(len(l)))
    return float(suma/int(num))
        

rep = int(input())
for _ in range (rep):
    line = input()
    l = line.split()
    medium = med(l[1:], l[0])
    total_sum = sum(float(l[i+1]) > medium for i in range(len(l[1:])))
    total_sum = (total_sum/int(l[0]))*100
    print('%.3f' %total_sum, end='%\n')
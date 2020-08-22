est = int(input())
days = 0
printers = 1

while(True):
    if(printers >= est/2):
        if(printers >= est):
            print(days + 1)
        else:
            print(days + 2)
        break
    else:
        printers = 2*printers
        days += 1
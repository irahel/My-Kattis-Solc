entry = input()
while(entry != "END"):
    count = 1
    while(True):
        prox = str(len(entry))
        if prox == entry:
            print(count)
            break;
        entry = prox
        count += 1
    entry = input()
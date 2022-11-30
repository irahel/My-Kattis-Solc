total = 0
res = ""
for i in range(5):
    a = input()
    if a.find("FBI") != -1:
        total += 1
        res += f"{str(i + 1)} "

if total == 0:
    print("HE GOT AWAY!")
else:
    print(res)
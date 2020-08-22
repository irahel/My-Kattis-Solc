count = int(input())

for _ in range(count):
    sum = input()
    if sum[0] == 'P':
        print("skipped")
    else:
        sum_ = sum.split('+')
        print(int(sum_[0])+int(sum_[1]))
A, B = input().split()

a = [int(A[0]), int(A[1]), int(A[2])]
b = [int(B[0]), int(B[1]), int(B[2])]

if a[2] > b[2]:
    print(f"{A[2]}{A[1]}{A[0]}")
elif a[2] < b[2]:
    print(f"{B[2]}{B[1]}{B[0]}")
elif a[1] > b[1]:
    print(f"{A[2]}{A[1]}{A[0]}")
elif a[1] < b[1]:
    print(f"{B[2]}{B[1]}{B[0]}")
elif a[0] > b[0] or a[0] >= b[0]:
    print(f"{A[2]}{A[1]}{A[0]}")
else:
    print(f"{B[2]}{B[1]}{B[0]}")
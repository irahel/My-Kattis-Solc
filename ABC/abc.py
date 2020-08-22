number_1, number_2, number_3 = input().split()
order = input()

number_1 = int(number_1)
number_2 = int(number_2)
number_3 = int(number_3)

minimum = min([number_1, number_2, number_3])
maximum = max([number_1, number_2, number_3])

medium = number_1
if number_2 > minimum and number_2 < maximum:
    medium = number_2
elif number_3 > minimum and number_3 < maximum:
    medium = number_3

end_str = ""

for i in (0, 1, 2):
    if order[i] == 'A':
        end_str += str(minimum)
    elif order[i] == 'B':
        end_str += str(medium)
    else:
        end_str += str(maximum)

    if i != 2:
        end_str += " "

print(end_str)
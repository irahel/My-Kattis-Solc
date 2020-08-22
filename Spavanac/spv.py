hours, minutes = input().split()

hours = int(hours)
minutes = int(minutes)

n_minutes = minutes - 45
n_hours = hours

if n_minutes < 0:
    if n_hours > 0:
        n_hours = hours - 1
    else:
        n_hours = 23
    n_minutes += 60

end_str = "" + str(n_hours) +" " +str(n_minutes)
print(end_str)
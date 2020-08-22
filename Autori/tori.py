hifen_name = input().split('-')
end_str = ""
for i in hifen_name:
    end_str += i[0]
print(end_str)
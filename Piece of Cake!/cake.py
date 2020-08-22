def volume(h, v):
    return h * v * 4

entry = input()
length, horizontal_cut, vertical_cut = entry.split( )

length = int(length)
horizontal_cut = int(horizontal_cut)
vertical_cut = int(vertical_cut)

piece_1 = volume(horizontal_cut, vertical_cut)
piece_2 = volume(horizontal_cut, length - vertical_cut)

piece_3 =  volume(length - horizontal_cut, vertical_cut)
piece_4 =  volume(length - horizontal_cut, length - vertical_cut)

bigger = piece_1

if(piece_2 > bigger):
    bigger = piece_2

if(piece_3 > bigger):
    bigger = piece_3

if(piece_4 > bigger):
    bigger = piece_4

print(bigger)
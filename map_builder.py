from random import *

# map builder
map_width = 12
map_height = 12
map_total = map_width * map_height
squares = []
terrain_types = ["grass", "desert", "snow"]

# build square array
X_coord_count = 0
Y_coord_count = 0
row_count = 0

print("squares: " + str(map_total))

for x in range(0, map_total):
    if X_coord_count >= map_width:
        X_coord_count = 0
        Y_coord_count += 1
        row_count += 1
    
    squares.insert( x,[X_coord_count,Y_coord_count,terrain_types[randint(0,2)]])

    X_coord_count += 1

print("rows: " + str(row_count+1))
print(squares)
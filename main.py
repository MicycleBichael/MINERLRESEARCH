import pyzelda

# create a new random dungeon with a size of 10 rooms
dungeon = pyzelda.generate_dungeon(10)

# print out the dungeon layout
print(dungeon.layout)

# save the dungeon to a file
dungeon.save("dungeon.txt")
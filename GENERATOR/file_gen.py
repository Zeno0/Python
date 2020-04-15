import os

root = "GENERATOR/music"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        # print(directories)
        # print(files)
        # input()
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f.strip('.emp3').split('-')
            # print("\t{}".format(f))
            print(song_details) 
        print('><' *50)

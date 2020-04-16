import os
import fnmatch

def find_music(start, extension):
    for path, directories, files, in os.walk(start):
        for file in fnmatch.filter(files, '*.{}' .format(extension)):
            absolute_path = os.path.abspath(path)
            yield os.path.join(absolute_path, file)


for f in find_music('GENERATOR/music', 'emp3'):
    print(f)
import shelve
print(dir())
for i in dir(__doc__):
    print(i)
print('-'*50)
print(dir(shelve))

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
       print(obj)
print('-'*50)
help(shelve.open)
print('-'*50)
help(shelve)



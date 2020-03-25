my_list = ["new#1","new#2","new#3","new#4"]
s = "asdfghjklpoiuytrewqazxcvbnm"
print(my_list)
string = ''
for i in my_list:
    string += i +' '
print(string)

string1 = ",".join(my_list)
print(string1)
print('$'.join(s))
print('#' * 60)

# dictionary  of locations
locations = {0:"You are in front of your laptop",
             1:"You at the solitary road",
             2:"you are at the hill",
             3:"you are at the building",
             4:"you are at the valley, Be Carefull",
             5:"you are in the  forset, Don't get lost"}
# list of exists 
exits = [{"Q":0},
         {"W":2,"E":3,"N":5,"S":4,"Q":0},
         {"N":5,"Q":0},
         {"W":1,"Q":0},
         {"N":1,"W":2,"Q":0},
          {"W":2,"S":1,"Q":0}]


# LOCATIONS AND EXITS ARE CREATED USING 'sample' pic

loc = 1 # default location is 1 i.e at the road

while False: # to run this loop just type "True" in while loop
   
    ava_exit = ", " .join(exits[loc].keys())
    print(locations[loc])

    if loc == 0:  #to exit from while loop and prints the value at 0 key of locations
        break

    dir = input("Available exits are: "+ava_exit+" ").upper()  # .upper() is to convert input un uppercase
    print()
    if dir in exits[loc]:
        loc = exits[loc][dir] # update the location
    else:
        print("You  can't go there ")
# this variable is used to create 'exits_' as a dictionary
exits_ = {0:{"Q":0},
          1:{"W":2,"E":3,"N":5,"S":4,"Q":0},
          2:{"N":5,"Q":0},
          3:{"W":1,"Q":0},
          4:{"N":1,"W":2,"Q":0},
          5:{"W":2,"S":1,"Q":0}}
vocab = {"QUIT" : "Q",
         "NORTH" : "N",
         "SOUTH" : "S",
         "EAST" : "E",
         "WEST" : "W"} 

while True:
    ava_exit = ", " .join(exits_[loc].keys())
    print(locations[loc])

    if loc == 0:  #to exit from while loop and prints the value at 0 key of locations
        break

    dir = input("Available exits are: "+ava_exit+" ").upper()  # .upper() is to convert input un uppercase
    print()
    if len(dir)>1:  # it will check if len of input is greater the 1 or not
        words = dir.split()  # it is helpful when there is 100s of dictionary
        for word in words:
            if word in vocab:
                dir = vocab[word]
                break
    if dir in exits_[loc]:
        loc = exits_[loc][dir] # update the location
    else:
        print("You  can't go there ")
print('-' * 50)
# showing how to use split() function
print(locations[0].split())
print(locations[3].split(","))
print(' '.join(locations[0].split()))

for i in locations[0].split():
    print(i)
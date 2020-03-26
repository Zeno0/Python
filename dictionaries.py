#creating and printing sample dictionary
sample = {"#1key":"#1value",
          "#2key":"#2value",
          "#3key":"#3value",
          "#4key":"#4value"}
print("Printing the sample dictionary: {}".format(sample))

#entering data into a dictionary
sample["#5key"] = "#5value"
print("sample after inputing new entry: {}".format(sample))
#printing particular value by using key
print(sample["#2key"])

#deleting an entry
del sample["#5key"]
print("Sample after deleting the last entry: {} ".format(sample))

# to ask key from the user and returning them the value
while True:
    key = input("Enter what you want to search in sample\n")
    if key == "quit":
        break
    if key in sample:
        #print(sample[key])
        val = sample.get(key)
        print(val)
    else :
        print(key +" doesn't exist")
# to ask key and value from the user to enter it in the sample dictionary
while True:
    key =input("Enter the key you want to add\n")
    if key == "quit":
        break
    val =input("enter coresponding value of the key\n")
    if key != "quit":
        sample[key]=val
    print("\t above mentioned key and value added")
print(sample)

# using different methods of dictionaries
for i in sample:
    print(i,end=' ')
    print("is key of value ",end='') 
    print(sample[i])

list_of_keys = sample.keys()
print(list_of_keys)

for i in sample.values():
    print(i)

print(sample.items())
k = sample.keys()
print(k)
sample["#00key"] = "#00value"   # to check k variable will be updated or not
print(k)

# entering the dictionary into a tuple
d_tuple = tuple(sample.items())
print(d_tuple)
print("now loop of tuple is running: ")
for i in d_tuple:
    k,v=i
    print("{} is key of value - {}" .format(k,v))
# now tuple to dictionary 
print(dict(d_tuple))
#creating and printing sample dictionary
sample = {"#1key":"#1value","#2key":"#2value","#3key":"#3value","#4key":"#4value"}
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


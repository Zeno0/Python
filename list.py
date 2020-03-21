# using count method in list
x = "aasdbasjbdbfdslknanankasnxaqwertyuioplkjhgfdsazxcvbnmsapxmihasxvnm"
for i in ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"):
    n = x.count(i)
    print(i)
    print("Count for {} in {} is {}" .format(i,x,n))

# another example of list
even = [2,4,6,8]
odd = [1,3,5,7,9]
newlist = even + odd
print(" first list is {} and then second list is {}, now their sum will be {}" .format(even,odd,newlist))
newlist.sort()
print(newlist)
# another way of sorting 
newlist.sort(reverse=True)
print(newlist)
# using list() function's constructor
print(list("this is just a sample"))
#using list
number = [even,odd]
print(number)
for number_set in number:
    print(number_set)
    for value in number_set:
        print(value)
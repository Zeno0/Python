set_sample = {"val1","val2","val3","val4"}
print(set_sample)

for i in set_sample:
    print(i)

# It is best to use the set() constructor to create a set

print("-" * 50)
empty_set = set()
print(empty_set)
empty_set.add("val1")
print(empty_set)

numbers = set(range(0,50))
print("Printing numbers set: {}".format(numbers))
print()
# There is no order in sets
sample_tuple = (4,16,25,36,49,64,81,100)
squares = set(sample_tuple)
print("Printing squares set: {}".format(squares))
print()
#using union
print("Printing Union of numbers and squares: {} ".format(numbers.union(squares)))
print()
#using intersection
print("Printing Intersection of numbers and squares: {} ".format(numbers.intersection(squares)))
print()
#print(numbers & new_set) It is same as intersection
# using difference
print("Printing difference of numbers and squares: {}" .format(numbers.difference(squares)))
# numbers - squares can also be used
print()

print("Printing the symmetric difference: {} ".format(numbers.symmetric_difference(squares)))
print()
num = {4,6,12,34,22,19}
print("Printing num set: {} ".format(num))
if num.issubset(numbers):
    print("num is subset of numbers")
if numbers.issuperset(num):
    print("numbers is superset of num")
print('-' * 60)
print(numbers)
val = int(input("enter what you want to be removed from the above set \n"))
if val in numbers:
    numbers.remove(val)
    print("{} is removed " .format(val))
    print("now numbers set is: {}" .format(numbers))
else:
    print("Is everything right with your head..?")
print("#" * 60)
sample_text = "this is just a sample, where vowels are going to be removed"
vowels = frozenset("aeiou")
print(vowels)
print(set(sample_text))
answer_set = set(sample_text).difference(vowels)
print(answer_set)
print(sorted(answer_set))



import sys

def my_range(n: int):
    print("My_range starts")
    start = 0
    while start <n:
        print("My_range is returning {}" .format(start))
        yield start
        start += 1

# _ = input("Line 11")
big_range = my_range(5)
# _ = input("Line 13")

print(next(big_range))
print("big_range in bytes is :{}".format(sys.getsizeof(big_range)))

big_list = []

# _= input("Line 19")
for val in big_range:
    # _ = input(" Line 21 - inside loop")
    big_list.append(val)

print("Big_list size in bytes :{}" .format(sys.getsizeof(big_range)))
print(big_range)
print(big_list)

print("looping or not....")
for i in my_range(5):
    print(" i is {}" .format(i))

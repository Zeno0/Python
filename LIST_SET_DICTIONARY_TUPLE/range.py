# creating and using range
S_range_1 = range(1,100)
random = range(0,10000)
print(random)
print(S_range_1)
print(S_range_1.index(23))
print(S_range_1.index(7) == 6)

S_range_2 = range(7,10000,7)
S_range_3 = random[7:10000:7]

print( S_range_3 == range(7,10000,7))
#print(list(S_range_2))
print(S_range_3)
x = int(input('Enter any number you wish under 10000 \n'))
if x in S_range_2:
    print(' NUmber you entered is divisible by 7')
else:
    print('not divisible by 7')
print(list(S_range_2))
print('#' * 50)

for i in S_range_1[::-22]:
    print(i)
sample = "test to check"
print(sample[::2])  # it means that all 2nd index of string's character will be displayed

p = range(0,100,5)
o = p[::5]  # it means every 5th element will be in variable 'o'
print(list(p))
print(list(o))
for i in p:
    print(i)
for i in o:
    print(i)
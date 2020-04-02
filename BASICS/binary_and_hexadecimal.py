#printing binary numbers
for i in range(11):
    print("{0} in binary is {0:04b} " .format(i))  # '0:04b' it means that only 4 digits will be there in binary of 'i' and by default it will begin from right side. If it was '0:<04b' then it begin's from left side 
x = 0b1010100101011101
y = 0b1111100011101010
print("Value in variable 'x' in decimal form {}".format(x))
print("Value in variable 'y' in decimal form {}".format(y))
print("now their product is: %s" %(x*y))
# printing hexadecimal numbers

for i in range(41):
    print("{0} in hexadecimal is {0:02x}" .format(i))
x = 0x231abcf12
y = 0xf311Cc232
print("Value in variable 'x' in decimal form {}".format(x))
print("Value in variable 'y' in decimal form {}".format(y))
print("now their product is: %s" %(x*y))
#######################################################
#program to find the binary of decimal entered by the user between 0 and 65535
powers = []
val = []
for power in range(15,-1,-1):
    val.append(power)
    powers.append(2 ** power)
print(val)
print(powers)

# to get input from user
x = int(input("Enter any number you want"))
#now for loop to print binary
for power in powers:  # the loop will execute 16 times.
    print(x//power,end='') 
    x %=power 
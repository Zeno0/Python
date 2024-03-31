#printing binary numbers

while True:
    flag = input("enter 'bin' for binary loop \nenter 'hex' for hexadecimal loop \nenter 'extra' for extra content \nto exit enter e \n")
    
    if flag == 'bin':
        for i in range(4):
            print("{0} in binary is {0:0b} " .format(i))  
        # '0:04b' it means that only 4 digits will be there in binary of 'i' and by default it will begin
        # from right side. If it was '0:<04b' then it begin's from left side 
        x = 0b1010100101011101
        y = 0b1111100011101010
        # print("{0:<04b} ".format(3))
        print("Value in variable 'x' in decimal form {}".format(x))
        print("Value in variable 'y' in decimal form {}".format(y))
        print("now their product is: %s" %(x*y))
    # printing hexadecimal numbers
    
    if flag == 'hex':
        for i in range(16543,16550):
            print("{0} in hexadecimal is {0:0x}" .format(i))
        x = 0x231abcf12
        y = 0xf311Cc232
        print("Value in variable 'x' in decimal form {}".format(x))
        print("Value in variable 'y' in decimal form {}".format(y))
        print("now their product is: %s" %(x*y))
    
    if flag == 'e':
        break
    #######################################################
    #program to find the binary of decimal entered by the user between 0 and 65535
    
    if flag == 'extra':
        powers = []
        val = []
        for power in range(15,-1,-1):
            val.append(power)
            powers.append(2 ** power)
        print(val)
        print(powers)
        
        # to get input from user
        x = int(input("Enter any number you want\n"))
        #now for loop to print binary
        for power in powers:  # the loop will execute 16 times.
            print(x//power,end='\n')  # this symbol returns quoteint
            x %=power 
        print('\n')
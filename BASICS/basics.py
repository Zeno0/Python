# to print anything just invoke print method
print(" \n")
print('This is basics demo by Shekhar \n')

# using \n and \t efficiently
string1 = ' "Hola" is \n "hello" in \n Spanish'
string2 = ' "Konichiwa" is \t "hello" in \t Japanese \n'
print(string1)
print(string2)

# using .format and different ways to print 
print('There are 7 days in a week: {0},{1},{2},{3},{4},{5},{6},'.format('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'))
print('Hello my name is %s and I am %d years old \n' %("Shekhar",19))

# creating variables 
x=7

#creating for loop
print("Now printing the table of 7: \n")
for i in range(1,11):
    print("the {0} times {1} is {2}".format(x,i,i*x))

print('Now printing the square and cubes of number from 1 to 10 \n')
for i in range(1,11):
    print('Cube and Square of {0} is {1} and {2} respectively.'.format(i,i**2,i**3))  # double asterik(*) means to the power

# now taking input from the user    
x = input('enter your name \n')
print('hello '+x +'\n')


# print("\f g")

# print("\x g")

# print("\u g")

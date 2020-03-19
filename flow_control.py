# ask for age from the user
age = int(input('What is your age ?'))
print(age)

# use if else
if age >= 18:
    print('You are eligible to vote')
else:
    print('Come back to this portal after %d years' %(18-age))

# another example of if else

print('What is your name ?')
name = input()

print('So %s I want you to guess any number between 1 to 5 \n' %(name))
guess = int(input())

if guess == 1:
    print(' %s guessed %d' %(name,guess))
elif guess == 2:
    print(' %s guessed %d' %(name,guess))
elif guess == 3:
    print(' %s guessed %d' %(name,guess))
elif guess == 4:
    print(' %s guessed %d' %(name,guess))
elif guess == 5:
    print(' %s guessed %d' %(name,guess))
else :
    print(" {} is dumb enough that, he can't even guess a number between 1 and 5" .format(name))

# another example 

word = 'This is just a sample'
print(word)
char = input('Write any character..\n')

if char in word:
    print(" Damn you are a Psychic as '{0}' exist in '{1}' " .format(char,word))
else:
    print(" no problem if you can't guess ")

# another example

name = input("So this is just to pass time.... what is your name ? \n")
print("What is your age?, %s" %(name))
age = int(input())

if age >0 and age <= 10 :
    print("Kid your age is %d, right? %s" %(age,name))
    print("If you want any advice press 'Y' if you don't want just hit enter ")
    choice = input()
    if choice == 'Y':
        print("Watch anime and have great day %s" %(name))
    else:
        print("Its fine if you don't want any advice %s" %(name))
elif age > 10 and age <=20:
    print("your age is %d, right? %s" %(age,name))
    print("If you want any advice press 'Y' if you don't want just hit enter ")
    choice = input()
    if choice == 'Y':
        print("Watch anime and take good care of yourself %s" %(name))
    else:
        print("Its fine if you don't want any advice %s" %(name))
elif age > 20 and age <=40:
    print("your age is %d, right? %s" %(age,name))
    print("If you want any advice press 'Y' if you don't want just hit enter ")
    choice = input()
    if choice == 'Y':
        print("10 beer in a day keeps the tension away.. rigth? %s" %(name))
    else:
        print("Its fine if you don't want any advice %s" %(name))
elif age > 40 and age <=60:
    print("your age is %d, right? %s" %(age,name))
    print("If you want any advice press 'Y' if you don't want just hit enter ")
    choice = input()
    if choice == 'Y':
         print("No advice from me lol, %s ♣" %(name))
    else:
        print("Its fine if you don't want any advice %s" %(name))

else :
    print("your age is over 60 right? %s " %(name))

# sample of using for loop

newword = "This a sample for 'for' loop "
print("1st for loop will run............................................................")
for i in range(0,len(newword)):
    print(newword[i])
print("2nd for loop will run............................................................")
for i in range(0,len(newword)):
    if newword[i] in "sample":
        print(newword[i])
print("3rd for loop will run............................................................")
for i in ("first","Second","third","no more","problems"):
    print("sample reached at {} state".format(i))
print("4th for loop will run............................................................")
for i in range(0,100,20):
    print("value of i = {}" .format(i))
print("5th for loop will run............................................................")
for i in range(0,5):
    for j in range(i,5):
       print("*",end='')
    print("")

# code to calculate the length of each segment of an ip address
ip = input("Enter the ip address ")
segment =1
segment_length = 0

for char in ip:
    if char == '.':
        print("segment {} contains lenght of {} " .format(segment,segment_length))
        segment +=1
        segment_length=0
    else:
        segment_length += 1
# This is to print last segment
if char != ".":
    print("segment {} contains length of {}" .format(segment,segment_length))
sample = open("/Users/RELIANCE/Desktop/sample.txt",'r') # 'r' means read only 
# type the path correctly to get output
for line in sample :
    #print(line)
    if "youth" in line.lower():
        print(line,end='')


sample.close() 
print('-' * 50)
######### ANOTHER WAY IS #########
with open("HANDELING_FILE\sample.txt",'r') as samp :  # it means that your sample.txt and python file is in the same directory
    for line in samp:              # also no need to close as 'with' takes care of that
        if "YOUTH" in line.upper():
            print(line,end='')

print('-' * 50)
with open("HANDELING_FILE\sample.txt",'r') as samp : 
    line = samp.readline()
    while line:
        print(line,end='')
        line = samp.readline()

print()
print('-' * 50) 


with open("HANDELING_FILE\sample.txt",'r') as sampe : 
    lines = sampe.readlines()  
print(lines) # printed in the form of list

print('-' * 50)
print()
for i in lines[::-1]:
    print(i)

print('-' * 50)
print()
#### to print line backwards ####
with open("HANDELING_FILE\sample.txt",'r') as s:
    l = s.read()

for x in l[::-1]:
    print(x,end='')



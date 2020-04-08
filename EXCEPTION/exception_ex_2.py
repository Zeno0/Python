def getint(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("INvaLId NUmbER, PLeaSE TRy AGaiN ")

first_num = getint("Please enter the first number ")
second_num = getint("Please enter the second number ")

try:
    print("{} divided by {} is {}" .format(first_num, second_num, first_num/second_num))   
except ZeroDivisionError:
    print("YOu CAn't DIviDE BY ZEro")

print("Program terminating")


def random_():
    width =69
    text = " just a random text"
    margin = (width - len(text))//2
    print(" "* margin,text)
    
def random_center_0(text):
    text = str(text)
    margin = (69 - len(text))//2
    print(" "* margin,text,margin)

def random_center_1(*args):
    text = " ".join(str(args))
    margin = (69 - len(text))//2
    print(" "* margin,text,margin)

def random_center_2(*args, sep=' ', end='\n', file=None, flush=False):
    text=""
    for i in args:
        text = text + str(i) + sep
    margin = (69 - len(text))//2
    print(" "* margin,text,end=end, file=file, flush=flush)

print("\t Using random() function: ")
random_()
print('-'*50)    
print("\t Using random_center_0() function: ")
random_center_0("another random text")
random_center_0("random text incoming")
print('-'*50)
print("\t Using random_center_1() function: ")
random_center_1(234)
random_center_1("Integer", "like", 1, 2, 3, "can also be passed")
print('-'*50)
print("\t Using random_center_2() function: ")
random_center_2("final function","example,", "Integers like", 1, 2, 3, "can also", "be passed",sep=':')

# now creating the file and writing into it using the function

with open("centered",mode='w') as centered_file:
    random_center_2("now passing the text into a file", file= centered_file)
    random_center_2("final function","example,", "Integers like", 1, 2, 3, "can also", "be passed",sep=':', file= centered_file)
    
# creating return type function

def random_center_(*args, sep=' '):
    text=""
    for i in args:
        text = text + str(i) + sep
    margin = (69 - len(text))//2
    return " "* margin+text
print('-'*50)
print(random_center_("another random text"))
print(random_center_("random text incoming"))


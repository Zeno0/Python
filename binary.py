# Creating a binary file 
# for creating and writing into a binary file 'bw' is used

with open("binary",'bw') as binary_file:
    for i in range(20):
        binary_file.write(bytes([i]))

with open("binary", 'br') as bin_file:
    for b in bin_file:
        print(b)
# In output x07 is for a <sound - beep>, to listen it, open the terminal in the binary file directory and enter - "cat binary" 

a= 65455
b= 98789
c= 12430
d= 12345

with open("binary2",'bw') as bin2:
    bin2.write(a.to_bytes(2,'big'))
    bin2.write(b.to_bytes(4,'big'))
    bin2.write(c.to_bytes(2,'big'))
    bin2.write(d.to_bytes(2,'big'))

with open("binary2",'br') as bin:
    e = int.from_bytes(bin.read(2), 'big')
    print(e)
    f = int.from_bytes(bin.read(4), 'big')
    print(f)
    g = int.from_bytes(bin.read(2), 'big')
    print(g)
    h = int.from_bytes(bin.read(2), 'big')
    print(h)
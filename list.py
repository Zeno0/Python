# using count method in list
x = "aasdbasjbdbfdslknanankasnxaqwertyuioplkjhgfdsazxcvbnmsapxmihasxvnm"
for i in ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"):
    n = x.count(i)
    print(i)
    print("Count for {} in {} is {}" .format(i,x,n))
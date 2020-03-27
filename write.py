characters = ["hachiman","yukino","yui","komachi"]
with open("char.txt",'w') as c:
    for i in characters:
        print(i,file=c)

######## now entering data from a file to a list #######

char_list = []

with open("char.txt",'r') as cha:
    for i in cha:
        char_list.append(i.strip('\n'))

print("now printing list: {}" .format(char_list) )

for i in char_list:
    print(i)

print('-' * 50)
print()

print("sample".strip('le'))

print('-' * 50)
print()

T_anime = "oregairu","hikigaya","yukino",28,"june",2013,((1,"youth rom-com is wrong, as I expected"),(2,"I'm sure everyone bears a worry of equal weight"),(3,"Sometime Gods of rom-com smiles upon you"),(4,"Basically, he has few friends"),(5,"And again, he returns from whence he came"),(6,"Finally, his and her beginning has ended"),(7,"Regardless, not getting a break over summer break"),(8,"One day, they shall learn the truth"),(9,"And yet again, he returns from whence he came"),(10,"While they remain as distance as they were, the festival shall soon encircle us "),(11,"And so, the curtain on each's stage rises, and the festival grows to a feast on us"),(12,"And so, his and her youths continue being wrong"),(13,"And so, their festival will never end"))                                    
with open("anime.txt",'w') as anime:
    print(T_anime, file=anime)

with open("anime.txt",'r') as ani:
    line = ani.readline()

anime_new = eval(line)
print(anime_new)
print('-' * 50)
print()
name, main_character, main_lead, date, month, year, no_of_episode = anime_new
print(name)
print(main_character)
print(main_lead)
print(date)
print(month)
print(year)
for i in no_of_episode:
    number, name =i
    print("Number is: {} and name is {} " .format(number,name))

print('-'*50)
print()
# using 'a' while writing on a .txt file
# 'a' is used to append the data on the file again and again, each time you runs the code,
# if you run  the following code 4 times then, there will be 4 times the same data on the file.
# When we use 'w' it just write one times.
    for i in range(1,11):
with open("sample.txt",'a') as table:   
        for j in range(1,11):
            print("{0} times {1} is {2}" .format(i,j,i*j), file=table)
        print('',file=table)

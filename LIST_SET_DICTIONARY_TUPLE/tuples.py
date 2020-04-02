#printing tuples
t = "a","b","c"
print("This is tuples: {}".format(t))
print("this ia normal: ""a","b","c")

T_anime = "oregairu","hikigaya","yukino",28,"june",2013,((1,"youth rom-com is wrong, as I expected"),(2,"I'm sure everyone bears a worry of equal weight"),(3,"Sometime Gods of rom-com smiles upon you"),(4,"Basically, he has few friends"),(5,"And again, he returns from whence he came"),(6,"Finally, his and her beginning has ended"),(7,"Regardless, not getting a break over summer break"),(8,"One day, they shall learn the truth"),(9,"And yet again, he returns from whence he came"),(10,"While they remain as distance as they were, the festival shall soon encircle us "),(11,"And so, the curtain on each's stage rises, and the festival grows to a feast on us"),(12,"And so, his and her youths continue being wrong"),(13,"And so, their festival will never end"))                                                          
T_anime_ = ["oregairu","hikigaya","yukino",10,"april",2020,(1,2,3,4,5,6,7,8,9,10,11,12,13)]
print("Another sample of tuple: {}".format(T_anime))
print(T_anime[0])
print(T_anime[1])
print(T_anime[2])
print(T_anime[3])
print(T_anime[4])
print(T_anime[5])

T_anime_[0] = "oregairu-SNAFU_S3"  # to change element like this you must use '[]' when creating tuple
print("Updated tuple: {}".format(T_anime_))


Anime_name, Main_Character, Main_lead, date, month, year , num_of_ep = T_anime
print(Anime_name)
print("Following is printed using variables:☺")
print(Main_Character)
print(Main_lead)
print(date)
print(month)
print(year)
print(num_of_ep)

T_anime_.append("yui")  # append is availabe for '[]' tuple not the simple tuple
print(T_anime_)
print("Now printing episodes: ")
for ep in num_of_ep:
    number , name = ep
    print(" Number of episode is: {} and name is: {}".format(number,name))



#swap in python
a =14
b =16
print("value of a={} and b={} " .format(a,b))
a,b = b,a
print("value of a={} and b={} after swap" .format(a,b))
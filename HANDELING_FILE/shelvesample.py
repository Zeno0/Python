import shelve

with shelve.open("HANDELING_FILE/test") as anime:
    anime["oregairu"] = "comedy,romance"
    anime["death note"] = "mystery,pyschological"
    anime["naruto"] = "adventute,action"
    anime["your name"] = "drama,romance"
    # when printing below lines indentation is really IMPORTANT
    print(anime["your name"])
    print(anime["oregairu"])
print(anime)

print('-'*50)

anime_1 = shelve.open("HANDELING_FILE/test2")
anime_1["oregairu"] = "comedy,romance"
anime_1["death note"] = "mystery,pyschological"
anime_1["naruto"] = "adventute,action"
anime_1["your name"] = "drama,romance"

for name in anime_1:
    print(name +' : '+ anime_1[name])
print(anime_1)

while True:
    anime_name = input("Enter the name of anime: \n")
    if anime_name == "quit":
        break
    #genre = anime_1[anime_name]
    genre = anime_1.get(anime_name,"we dont have "+anime_name+" yet")
    print(genre)
print('-'*50)
# TO get results in Alphabetical order 
ordered = sorted(anime_1.keys())
for i in ordered:
    print(i + " - "+ anime_1[i])

# using functions to make working easy
print('-'*50)
for i in anime_1.values():
    print(i)
print(anime_1.values())
print('-'*50)
for i in anime_1.items():
    print(i)
print(anime_1.items())
anime_1.close()



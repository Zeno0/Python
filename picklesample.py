# serialization in python
import pickle
anime = "oregairu","hikigaya","yukino","28","june","2013",((1,"youth rom-com is wrong, as I expected"), (2,"I'm sure everyone bears a worry of equal weight"),(3,"Sometime Gods of rom-com smiles upon you"))
        
with open("anime.pickle",'bw') as anime_bin:
    pickle.dump(anime,anime_bin,protocol=0) 

with open("anime.pickle",'br') as ani:
    a = pickle.load(ani)

print(a)
name, main_character, main_lead, date, month, year, number_of_episodes = a
print(name)
print(main_character)
print(main_lead)
print(date)
print(month)
print(year)
for i in number_of_episodes:
    number , name = i
    print(number,end=' ')
    print(name)

print('-' * 50)
print()
even_list = list(range(0,20,2))
odd_list = list(range(1,20,2))
with open("anime.pickle",'bw') as bin_for_all:
    # when protocol is 0 then binary file is much easier to understand
   # pickle.dump(anime,bin_for_all,protocol=0)
    pickle.dump(even_list,bin_for_all,protocol=0)
    pickle.dump(odd_list,bin_for_all,protocol=0)
    pickle.dump(14321,bin_for_all,protocol=0)

with open("anime.pickle",'br') as bin_for_all_out:
    even = pickle.load(bin_for_all_out)
    odd = pickle.load(bin_for_all_out)
    x = pickle.load(bin_for_all_out)

for i in even:
    print(i)

for i in odd:
    print(i)

print(x)

# command to delete the pickle file
#pickle.loads(b"cos\nsystem\n(S'del anime.pickle'\ntR.")
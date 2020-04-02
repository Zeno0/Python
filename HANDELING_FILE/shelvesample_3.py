import shelve
book = shelve.open("HANDELING_FILE/book_db")
book["anime"] = {"DBZ" : ["Goku","vegeta","gohan"],
                 "oregairu" : ["hachiman","yukino","yui"],
                 "naruto" : ["naruto","sasuke","sakura"],
                 "eureka7" : ["eruka","holland","renton"]}
book ["music"] = {"Green day" : ["American idiot", "21 Guns", "Extraordinary Girl"],
                  "Linkin park" : ["One more light", "iridescent", "In the end"]}

print(book["anime"])
print(book["music"])
print(book["anime"]["oregairu"])
book.close()
print('-'*50)

# modifing the previous dictionary_challenge to use shelve
locations = shelve.open('HANDELING_FILE/location')
vocabulary = shelve.open('HANDELING_FILE/vocabulary')

loc = "1"
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys())
 
    print(locations[loc]["desc"])
 
    if loc == '0':
        break
    else:
        allExits = locations[loc]['exits'].copy()
        allExits.update(locations[loc]["namedExits"])
 
    direction = input("Available exits are " + availableExits).upper()
    print()
 
    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        words = direction.split()
        for word in words:
            if word in vocabulary:   # does it contain a word we know?
                direction = vocabulary[word]
                break
 
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")

locations.close()
vocabulary.close()
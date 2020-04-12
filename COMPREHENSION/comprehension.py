print(__file__)

text = "Watching anime is the best"

capitals = [char.upper() for char in text]
words = [word.upper() for word in text.split(' ')]
lc_words = text.split(' ')
squares = [number **2 for number in range(1,7)]
cubes = {number **3 for number in range(1,7)}

print(capitals)
print(words)
print(lc_words)
print(squares)
print(cubes)
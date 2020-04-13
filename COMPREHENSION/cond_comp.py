anime = [['oregairu', 'spam', 'naruto'],
        ['oregairu', 'spam', 'naruto', 'your name'],
        ['oregairu', 'spam', 'naruto', 'your name', 'spam'],
        ['spam', 'naruto', 'your name', 'eureka7', 'spam'],
        ['oregairu', 'spam', 'naruto', 'your name', 'eureka7', 'spam'],
        ['oregairu', 'eureka7', 'naruto', 'your name'],
        ['oregairu', 'eureka7', 'your name']]


for name in anime:
    if "spam" not in name:
        print(name)
print("><"*40)
names = [name for name in anime if "spam" not in name and "naruto" not in name]
print(names)
print("><"*40)

# using conditional expression
x =15
exp = "twelve" if x==12 else "unknown"
print(exp)
print("><"*40)
for name in anime:
    print(name, "contains your name" if "your name" in name else " does not contain your name ")



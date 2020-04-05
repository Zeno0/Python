# create a class named kettle
class kettle(object):
    # this is the attribute for kettle class and it is same for each instance of kettle class
    power_source = "Electricity"

    # "__init__" this is like a constructor for class kettle
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
    
    #  1st method for kettle class, since 'self' is within parentheses, and whenever method is called within a class "self" must be used
    def switch_on(self):
        self.on = True

# first object of kettle class
kenwood = kettle("kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

# second object of kettle class
hamilton = kettle("hamilton", 14.55)

print("models: {}= {}, {}= {}" .format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print("Models: {0.make}= {0.price}, {1.make}= {1.price}" .format(kenwood, hamilton))

print('-'*50)
print(hamilton.on)
# using 1st method of kettle class
hamilton.switch_on()
print(hamilton.on)

print('-'*50)
print(kenwood.on)
kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)

print('-'*50)
kenwood.power = 23.561
print(kenwood.power)
# print(hamilton.power)  // It will show error since 'power' is not created for the hamilton

print('-'*50)
# Showing attribute
print(kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
# changing power_source 
kettle.power_source = "Atomic"
print(kettle.power_source)
# changing power_source for kenwood
kenwood.power_source = "Gas"
print(kenwood.power_source)
print(hamilton.power_source)


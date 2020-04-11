class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio >1:
            print("easypeasy, hell i am flying")
        elif self.ratio == 1:
            print("tough, but i can fly")
        else:
            print("can't fly, i am gonna walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("******WADDLE******")

    def swim(self):
        print("******SWIMMING******")
    
    def quack(self):
        print("******QUACK*******")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self._wing = Wing(0.8)
        self.fly = self.aviate
    
    def walk(self):
        print("*****WADDEL__TOO*****")

    def swim(self):
        print("*******FROZEN*******")

    def quack(self):
        print("*****I_DON'_QUACK*****")
    
    def aviate(self):
        print("I am alreday here, where you are migrating to")

    # def fly(self):
    #     self._wing.fly()   


class Mallard(Duck):
    pass

class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_met = getattr(duck, 'fly', None)
        if callable(fly_met):
        # if isinstance(duck, Duck):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, coz its a " + str(type(duck).__name__))

    def migrate(self):
        for duck in self.flock:
            try:
                duck.fly()
            except AttributeError:
                print("can't fly")
                # raise


def test(duck):
    duck.walk()
    duck.swim()
    duck.quack()


if __name__ == '__main__':
    din = Duck()
    test(din)
    din.fly()
    print('><'*50)
    per = Penguin()
    test(per)
    # per.fly()


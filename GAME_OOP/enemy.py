import random
class Enemy:
    def __init__(self, name="enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        rem_points = self.hit_points - damage
        if rem_points >=0:
            self.hit_points = rem_points
            print("Enemy took {} points damage and have {} points left ".format(damage, self.hit_points))
        else:
            self.lives -= 1
            self.hit_points = 12
            if self.lives > 0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead " .format(self))
                self.alive = False    

    def __str__(self):
        return "Name: {0.name}, Lives:{0.lives}, HP:{0.hit_points} " .format(self)


class Troll(Enemy):
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def grunt(self):
        print("Me {0.name}, {0.name} stomps you" .format(self))


class Vampire(Enemy):
    
    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def dodges(self):
        if random.randint(1,3) == 3:
            print("***********{0.name} DODGES*********" .format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)


class Vampireking(Vampire):
    def __init__(self,name):
        super().__init__(name=name)
        self.hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage // 4)


    



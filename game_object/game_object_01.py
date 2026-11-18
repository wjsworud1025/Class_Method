class GameObject:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def info(self):
        return f"{self.name} ({self.x}, {self.y})"
class Character(GameObject):
    pass

class Warrior(Character):
    pass

class Wizard(Character):
    pass

class Monster(GameObject):
    def __init__(self, name, power, x=0, y=0):
        super().__init__(name, x, y)
        self.power = power

class Dragon(Monster):
    pass

class Slime(Monster):
    pass

d = Dragon("드래곤", 50)
d.move(3, 4)
print(d.info())
print(isinstance(d, Monster), isinstance(d, GameObject), isinstance(d, Character))
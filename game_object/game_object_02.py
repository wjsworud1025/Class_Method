class HP:
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current = max_hp 

    def damage(self, amount):
        self.current = max(self.current - amount, 0)

    def is_alive(self):
        if self.current > 0:
            return True

class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power

class Skill:
    def __init__(self, name, multipler):
        self.name = name
        self.multipler = multipler

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

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
    def __init__(self, name, max_hp, weapon, skill, armor):
        super().__init__(name)
        self.hp = HP(max_hp)
        self.weapon = weapon
        self.skill = skill
        self.armor = armor

    def attack(self):
        return self.weapon.power

    def use_skill(self):
        return int(self.weapon.power * self.skill.multipler)

    def take_damage(self, amount):
        damage = max(amount - self.armor.defense, 0)
        before_hp = self.hp.current
        self.hp.damage(damage)
        return before_hp - self.hp.current
    
    def change_weapon(self, weapon):
        self.weapon = weapon

class Warrior(Character):
    def __init__(self, name):
        super().__init__(
            name,
            max_hp=150,
            weapon=Weapon("롱소드", 20),
            skill=Skill("강타", 1.5),
            armor=Armor("판금갑옷", 10)
        )

class Wizard(Character):
    def __init__(self, name):
        super().__init__(
            name,
            max_hp=90,
            weapon=Weapon("지팡이", 8),
            skill=Skill("파이어볼", 4.0),
            armor=Armor("로브", 2)
        )

class Monster(GameObject):
    def __init__(self, name, power, x=0, y=0):
        super().__init__(name, x, y)
        self.power = power

class Dragon(Monster):
    pass

class Slime(Monster):
    pass


w = Warrior("아서")
z = Wizard("멀린")

print(w.attack(), w.use_skill(), z.use_skill())

print(w.take_damage(25), w.hp.current)

print(z.take_damage(25), z.hp.current), w.change_weapon(Weapon("전투도끼", 30))

print(w.attack(), w.use_skill())
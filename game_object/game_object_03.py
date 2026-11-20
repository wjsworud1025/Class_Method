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
class HP:
    def __init__(self, max_hp):
        self.max_hp = max_hp
        self.current = max_hp
    def damage(self, amount):
        self.current = max(self.current - max(amount, 0), 0)
    def heal_full(self):
        self.current = self.max_hp
    def is_alive(self):
        return self.current > 0
class Item:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
class Element:
    def __init__(self, name):
        self.name = name
    def multiplier(self, target):
        counter = {"불": "풀", "풀": "물", "물": "불"}
        if self.name == target.name:
            return 1.0
        elif counter[self.name] == target.name:
            return 2.0
        else:
            return 0.5
    def __str__(self):
        return self.name
class Weapon(Item):
    def __init__(self, name, power, element):
        super().__init__(name)
        self.power = power
        self.element = element  # Element 객체를 가진다: 구성
        self.enhance = 0
    def upgrade(self):
        self.enhance += 1
        self.power += 5
    def __str__(self):
        if self.enhance == 0:
            return f"{self.name}[{self.element}]"
        return f"+{self.enhance} {self.name}[{self.element}]"
class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
    def add(self, item):
        if len(self.items) >= self.capacity:
            return False
        self.items.append(item)
        return True
    def take(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return item
        return None
class Character(GameObject):
    def __init__(self, name, max_hp, weapon):
        super().__init__(name)
        self.base_hp = max_hp
        self.hp = HP(max_hp)
        self.weapon = weapon
        self.level = Level()
        self.inventory = Inventory(5)
    def attack(self, target):
        if not target.hp.is_alive():
            return [f"{target.name}은(는) 이미 처치되었습니다."]

        mult = self.weapon.element.multiplier(target.element)
        damage = int(self.weapon.power * mult)
        target.take_damage(damage)
        log = [
            f"{self.name}의 {self.weapon} 공격! "
            f"{target.name}에게 {damage} 피해 (x{mult})"
        ]

        if target.hp.is_alive():
            return log

        log.append(f"{target.name} 처치! EXP +{target.exp_reward}")
        up = self.gain_exp(target.exp_reward)
        if up:
            log.append(f"레벨 업! Lv.{self.level.level} (최대 HP {self.hp.max_hp})")

        if target.drop is not None:
            if self.inventory.add(target.drop):
                log.append(f"'{target.drop.name}' 획득!")
            else:
                log.append(f"인벤토리가 가득 차서 '{target.drop.name}'을(를) 얻지 못했습니다.")
        return log
    def take_damage(self, amount):
        before_hp = self.hp.current
        self.hp.damage(max(amount, 0))
        return before_hp - self.hp.current
    def change_weapon(self, weapon):
        self.weapon = weapon
    def gain_exp(self, amount):
        up = self.level.gain(amount)
        new_max_hp = self.base_hp + (self.level.level - 1) * 20
        if new_max_hp > self.hp.max_hp:
            self.hp.max_hp = new_max_hp
            self.hp.heal_full()
        return up
    def equip(self, name):
        item = self.inventory.take(name)
        if item is None:
            return False
        if not isinstance(item, Weapon):
            self.inventory.add(item)
            return False

        self.inventory.add(self.weapon)
        self.change_weapon(item)
        return True
    def upgrade_weapon(self):
        stone = self.inventory.take("강화석")
        if stone is None:
            return False
        self.weapon.upgrade()
        return True
class Level:
    def __init__(self, level=1, exp=0):
        self.level = level
        self.exp = exp
    def need(self):
        return self.level * 100
    def gain(self, amount):
        self.exp += amount
        up = 0
        while self.exp >= self.need():
            self.exp -= self.need()
            self.level += 1
            up += 1
        return up
class Warrior(Character):
    def __init__(self, name):
        super().__init__(
            name,
            max_hp=150,
            weapon=Weapon("화염검", 30, Element("불"))
        )
class Monster(GameObject):
    def __init__(self, name, max_hp, element, exp_reward, drop=None, x=0, y=0):
        super().__init__(name, x, y)
        self.hp = HP(max_hp)
        self.element = element  # Element 객체
        self.exp_reward = exp_reward
        self.drop = drop        # Item 객체 또는 None
    def take_damage(self, amount):
        before_hp = self.hp.current
        self.hp.damage(amount)
        return before_hp - self.hp.current
class Dragon(Monster):
    def __init__(self):
        super().__init__(
            name="레드 드래곤",
            max_hp=300,
            element=Element("불"),
            exp_reward=500,
            drop=None,
        )
class Slime(Monster):
    def __init__(self):
        super().__init__(
            name="이끼 슬라임",
            max_hp=40,
            element=Element("풀"),
            exp_reward=60,
            drop=Weapon("물의 창", 25, Element("물")),
        )
class Golem(Monster):
    def __init__(self):
        super().__init__(
            name="네스트골렘",
            max_hp=120,
            element=Element("풀"),
            exp_reward=90,
            drop=Item("강화석"),
        )

hero = Warrior("아서")

# 1) 슬라임 사냥
for line in hero.attack(Slime()):
    print(line)
print([i.name for i in hero.inventory.items])
print("---")

# 2) 골렘 사냥 (쓰러질 때까지 공격)
golem = Golem()
while golem.hp.is_alive():
    for line in hero.attack(golem):
        print(line)
print("---")

# 3) 보스전 준비: 무기 교체 + 강화
print(hero.equip("물의 창"), hero.weapon, [i.name for i in hero.inventory.items])
print(hero.upgrade_weapon(), hero.weapon, hero.weapon.power)
print("---")

# 4) 보스전
boss = Dragon()
turn = 0
while boss.hp.is_alive():
    turn += 1
    hero.attack(boss)
print(f"{turn}턴 만에 보스 처치! Lv.{hero.level.level}, EXP {hero.level.exp}")
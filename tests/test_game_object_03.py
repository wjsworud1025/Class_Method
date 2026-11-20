import unittest

from game_object.game_object_03 import (
    Dragon, Element, Golem, HP, Item, Level, Slime, Warrior, Weapon,
)


class BattleTests(unittest.TestCase):
    def test_quest_reaches_level_four_after_five_boss_attacks(self):
        hero = Warrior("아서")
        hero.take_damage(100)
        slime = Slime()
        logs = hero.attack(slime)
        self.assertIn("60 피해 (x2.0)", logs[0])
        self.assertEqual(slime.hp.current, 0)
        self.assertEqual((hero.level.level, hero.level.exp, hero.hp.current), (1, 60, 50))

        golem = Golem()
        self.assertEqual(len(hero.attack(golem)), 1)
        self.assertEqual(golem.hp.current, 60)
        logs = hero.attack(golem)
        self.assertIn("레벨 업! Lv.2 (최대 HP 170)", logs)
        self.assertEqual((hero.level.exp, hero.hp.current, hero.hp.max_hp), (50, 170, 170))

        self.assertTrue(hero.equip("물의 창"))
        self.assertTrue(hero.upgrade_weapon())
        self.assertEqual(str(hero.weapon), "+1 물의 창[물]")
        boss = Dragon()
        for remaining_hp in (240, 180, 120, 60, 0):
            hero.attack(boss)
            self.assertEqual(boss.hp.current, remaining_hp)
        self.assertEqual((hero.level.level, hero.level.exp, hero.hp.current), (4, 50, 210))

    def test_dead_target_does_not_repeat_rewards(self):
        hero = Warrior("아서")
        slime = Slime()
        hero.attack(slime)
        items = hero.inventory.items.copy()
        hero.attack(slime)
        self.assertEqual(hero.level.exp, 60)
        self.assertEqual(hero.inventory.items, items)

    def test_full_inventory_rejects_drop_but_awards_experience(self):
        hero = Warrior("아서")
        for _ in range(5):
            hero.inventory.add(Item("돌"))
        logs = hero.attack(Slime())
        self.assertEqual(hero.level.exp, 60)
        self.assertEqual(len(hero.inventory.items), 5)
        self.assertTrue(all(item.name == "돌" for item in hero.inventory.items))
        self.assertIn("가득", logs[-1])

    def test_weak_attack_truncates_damage(self):
        hero = Warrior("아서")
        hero.change_weapon(Weapon("물의 창", 25, Element("물")))
        slime = Slime()
        logs = hero.attack(slime)
        self.assertEqual(slime.hp.current, 28)
        self.assertIn("12 피해 (x0.5)", logs[0])
        self.assertEqual(hero.level.exp, 0)


class GrowthAndEquipmentTests(unittest.TestCase):
    def test_experience_returns_each_level_gained(self):
        level = Level()
        self.assertEqual((level.gain(150), level.level, level.exp), (1, 2, 50))
        self.assertEqual((level.gain(500), level.level, level.exp), (2, 4, 50))
        hero = Warrior("아서")
        self.assertEqual(hero.gain_exp(650), 3)
        self.assertEqual((hero.hp.current, hero.hp.max_hp), (210, 210))

    def test_full_inventory_equips_without_losing_items(self):
        hero = Warrior("아서")
        sword = hero.weapon
        spear = Weapon("물의 창", 25, Element("물"))
        hero.inventory.add(spear)
        stone = Item("강화석")
        hero.inventory.add(stone)
        for _ in range(3):
            hero.inventory.add(Item("돌"))
        self.assertTrue(hero.equip("물의 창"))
        self.assertIs(hero.weapon, spear)
        self.assertIn(sword, hero.inventory.items)
        self.assertFalse(hero.equip("강화석"))
        self.assertIn(stone, hero.inventory.items)
        self.assertFalse(hero.equip("없는 무기"))
        self.assertEqual(len(hero.inventory.items), 5)

    def test_upgrade_consumes_one_stone_and_requires_another(self):
        hero = Warrior("아서")
        hero.inventory.add(Item("강화석"))
        hero.inventory.add(Item("강화석"))
        self.assertTrue(hero.upgrade_weapon())
        self.assertEqual((hero.weapon.power, hero.weapon.enhance), (35, 1))
        self.assertEqual(len(hero.inventory.items), 1)
        self.assertTrue(hero.upgrade_weapon())
        self.assertFalse(hero.upgrade_weapon())
        self.assertEqual((hero.weapon.power, hero.weapon.enhance), (40, 2))

    def test_damage_never_heals_or_reduces_hp_below_zero(self):
        hp = HP(150)
        hp.damage(-10)
        self.assertEqual(hp.current, 150)
        hp.damage(200)
        self.assertEqual(hp.current, 0)
        self.assertFalse(hp.is_alive())
        hp.heal_full()
        self.assertEqual(hp.current, 150)


if __name__ == "__main__":
    unittest.main()

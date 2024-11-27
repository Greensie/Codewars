# https://www.codewars.com/kata/66bdf9f511467a75cf5ff88b
from enum import Enum


class Actions(Enum):
    BUFF = 1
    NORMAL_ATTACK = 2
    SPECIAL_ATTACK = 3


class Hero:
    def __init__(self):
        self.name = "Hero"
        self.hp = 0
        self.power = 0
        self.next_damage_multiplayer = 0
        self.damage_to_op = 0
        self.loose_flag = 0

    def turn_as_first(self, action: Actions):
        return self.damage_to_op

    def react_to_op_turn(self, damage_suffered):
        return self.hp


class Warrior(Hero):
    def __init__(self):
        self.name = 'Warrior'
        self.hp = 260
        self.power = 40
        self.next_damage_multiplayer = 1
        self.damage_to_op = 40
        self.loose_flag = 0

    def turn_as_first(self, action: Actions):
        if action == Actions.BUFF:  # buff
            self.hp += 40
            self.next_damage_multiplayer = 0.5
            self.damage_to_op = 0
            return self.damage_to_op
        if action == Actions.NORMAL_ATTACK:  # normal attack
            self.damage_to_op = 40
            return self.damage_to_op
        if action == Actions.SPECIAL_ATTACK:  # special attack
            self.damage_to_op = 75
            return self.damage_to_op

    def react_to_op_turn(self, damage_suffered):
        self.hp = self.hp - self.next_damage_multiplayer * damage_suffered
        self.next_damage_multiplayer = 1
        if self.hp <= 0:
            self.loose_flag = 1
        return self.hp


class Mage(Hero):
    def __init__(self):
        self.name = 'Mage'
        self.hp = 200
        self.power = 50
        self.next_damage_multiplayer = 1
        self.damage_to_op = 50
        self.loose_flag = 0

    def turn_as_first(self, action: Actions):
        if action == Actions.BUFF:  # buff
            self.next_damage_multiplayer = 0.5
            self.damage_to_op = 0
            return self.damage_to_op
        if action == Actions.NORMAL_ATTACK:  # normal attack
            self.damage_to_op = 50
            return self.damage_to_op
        if action == Actions.SPECIAL_ATTACK:  # special attack
            self.damage_to_op = 90
            return self.damage_to_op

    def react_to_op_turn(self, damage_suffered):
        self.hp = self.hp - self.next_damage_multiplayer * damage_suffered
        self.next_damage_multiplayer = 1
        if self.hp <= 0:
            self.loose_flag = 1
        return self.hp


class Assassin(Hero):
    def __init__(self):
        self.name = 'Assassin'
        self.hp = 235
        self.power = 30
        self.next_damage_multiplayer = 1
        self.damage_to_op = 30
        self.loose_flag = 0
        self.buff_timer = 0

    def turn_as_first(self, action: Actions):
        if action == Actions.BUFF:  # buff
            self.buff_timer = 3
            self.damage_to_op = 0
            return self.damage_to_op
        if action == Actions.NORMAL_ATTACK:  # normal attack
            self.damage_to_op = 30
            if self.buff_timer > 0:
                self.damage_to_op = 70
                self.buff_timer -= 1
            return self.damage_to_op
        if action == Actions.SPECIAL_ATTACK:  # special attack
            self.damage_to_op = 60
            if self.buff_timer > 0:
                self.damage_to_op = 140
                self.buff_timer -= 1
            return self.damage_to_op

    def react_to_op_turn(self, damage_suffered):
        self.hp -= damage_suffered
        self.next_damage_multiplayer = 1
        if self.hp <= 0:
            self.loose_flag = 1
        return self.hp


class Battle:
    def __init__(self, class1: Hero, class2: Hero):
        self.is_over = 0
        self.hero1 = class1
        self.hero1_turn = class1.turn_as_first(Actions.NORMAL_ATTACK)
        self.hero1_react = class1.react_to_op_turn(0)
        self.hero2 = class2
        self.hero2_turn = class2.turn_as_first(Actions.NORMAL_ATTACK)
        self.hero2_react = class2.react_to_op_turn(0)
        self.hero1hp = class1.hp
        self.hero2hp = class2.hp
        self.hero1_name = class1.name
        self.hero2_name = class2.name

    def play_turn(self, action: Actions, action2: Actions):
        if self.hero1hp == 0 or self.hero2hp == 0:
            result = "This battle is over!"
            return result
        dmg1 = self.hero1_turn(action)
        self.hero2hp = self.hero2_react(dmg1)
        dmg2 = self.hero2_turn(action2)
        self.hero1hp = self.hero1_react(dmg2)
        result = self.hero1_name + " HP =" + self.hero1hp + ", " + self.hero2_name + " HP =" + self.hero2hp
        if self.hero1hp == 0 or self.hero2hp == 0:
            if self.hero1hp > self.hero2hp:
                result = "The" + self.hero1_name + "won! Remaining HP=" + self.hero1hp
            if self.hero2hp > self.hero1hp:
                result = "The" + self.hero2_name + "won! Remaining HP=" + self.hero2hp

        return result


beowulf = Warrior()
merlin = Mage()
epic_battle = Battle(beowulf, merlin)
epic_battle.play_turn(Actions.NORMAL_ATTACK, Actions.BUFF)

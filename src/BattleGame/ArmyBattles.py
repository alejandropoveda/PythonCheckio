# Taken from mission The Warriors


class Warrior:

    attack = 5

    def __init__(self):
        self.health = 50
        self.is_alive = True

    def receive_damage(self, damage):
        new_health = self.health - damage
        if new_health <= 0:
            self.health = 0
            self.is_alive = False
        else:
            self.health = new_health


class Knight(Warrior):
    attack = 7

    def __init__(self):
        Warrior.__init__(self)


class Army:

    def __init__(self):
        self.units: list = []

    def add_units(self, unit_type: Warrior, unit_number: int):
        i = 0
        while i < unit_number:
            self.units.append(unit_type())
            i += 1

    def next_unit(self) -> Warrior:
        return self.units.pop(0)

    def is_still_able_to_fight(self) -> bool:
        result = False
        if len(self.units) > 0:
            result = True

        return result


class Battle:

    @staticmethod
    def fight(army_1: Army, army_2: Army) -> bool:

        is_army_1_the_winner = False

        army_1_current_fighter = army_1.next_unit()
        army_2_current_fighter = army_2.next_unit()

        is_the_battle_over = False

        while not is_the_battle_over:
            is_army_1_unit_the_winner: bool = fight(army_1_current_fighter, army_2_current_fighter)
            if is_army_1_unit_the_winner:
                if army_2.is_still_able_to_fight():
                    army_2_current_fighter = army_2.next_unit()
                else:
                    is_army_1_the_winner = True
                    is_the_battle_over = True
            else:
                if army_1.is_still_able_to_fight():
                    army_1_current_fighter = army_1.next_unit()
                else:
                    is_the_battle_over = True

        return is_army_1_the_winner


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    result = False
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.receive_damage(unit_1.attack)
        if not unit_2.is_alive:
            result = True
        else:
            unit_1.receive_damage(unit_2.attack)

    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    print(chuck.is_alive)
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")

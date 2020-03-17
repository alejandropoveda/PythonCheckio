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
    #These "asserts" using only for self-checking and not necessary for auto-testing

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

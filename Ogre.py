from Enemy import *
import random
class Ogre(Enemy):

    def __init__(self, health_points=10, attack_damage=10):
        super().__init__(type_of_enemy="Ogre",
                         health_points=health_points,
                         attack_damage=attack_damage)

    def talk(self):
        print('Ogre is slamming hands all around')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.health_points += 4
            print('Ogre gets anget and increases attack by 4')

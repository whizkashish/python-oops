from Enemy import *
import random

class Zombie(Enemy):

    def __init__(self, health_points=10, attack_damage=10):
        super().__init__(type_of_enemy="Zombie",
                         health_points=health_points,
                         attack_damage=attack_damage)


    def talk(self):
        print('*Grumbling*')

    def spread_disease(self):
        print('The Zombie is trying to spread disease')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_points += 1
            print('Zombie regenerated 2HP!')

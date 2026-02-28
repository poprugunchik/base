import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100


    def attack(self, other):
        other.health -= 25
        print(f"{self.name} атаковал {other.name}."
              f"У {other.name} осталось {max(other.health, 0)} здоровья.")


warrior1 = Warrior("Геракл")
warrior2 = Warrior("Зевс")

while warrior1.health > 0 and warrior2.health > 0:
    attacker = random.choice([warrior1, warrior2])
    defender = warrior2 if attacker == warrior1 else warrior1
    attacker.attack(defender)

if warrior1.health > 0:
    print(f"Победил {warrior1.name}")

else:
    print(f"Победил {warrior2.name}")

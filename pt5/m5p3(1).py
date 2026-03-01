import random

class Warrior:
    def __init__(self, name, min_power, max_power):
        self.name = name
        self._health = 100
        self.min_power = min_power
        self.max_power = max_power

    @property
    def health(self):
        return self._health

    def is_alive(self):
        return self._health > 0

    def take_damage(self, amount):
        self._health -= amount
        self._health = max(self._health, 0)
        print(f"{self.name} получил {amount} урона. Осталось {self._health} HP.")

    def attack(self, other):
        damage = random.randint(self.min_power, self.max_power)
        print(f"{self.name} атакует {other.name} на {damage} урона!")
        other.take_damage(damage)


warrior1 = Warrior("Геракл", 10, 40)
warrior2 = Warrior("Зевс", 10, 40)

while warrior1.is_alive() and warrior2.is_alive():
    attacker = random.choice([warrior1, warrior2])
    defender = warrior2 if attacker == warrior1 else warrior1
    attacker.attack(defender)

winner = warrior1 if warrior1.is_alive() else warrior2
print(f"Победил {winner.name}")
import random

class Warrior:
    def __init__(self, name):
        self.name = name
        self._health = 100
        self._armor = 50
        self._stamina = 100

    @property
    def health(self):
        return self._health

    @property
    def armor(self):
        return self._armor

    @property
    def stamina(self):
        return self._stamina

    def is_alive(self):
        return self._health > 0

    def spend_stamina(self, amount):
        self._stamina = max(0, self._stamina - amount)

    def recover_stamina(self, amount=15):
        self._stamina = min(100, self._stamina + amount)
        print(f"{self.name} восстанавливает {amount} выносливости")

    def attack(self):
        if self._stamina < 10:
            print(f"{self.name} слишком устал, чтобы атаковать!")
            return 0  # ноль урона
        self.spend_stamina(10)
        damage = random.randint(10, 30)  # случайная сила удара
        print(f"{self.name} готовит атаку на {damage} урона")
        return damage

    def take_damage(self, damage):
        if self._armor > 0:
            armor_loss = random.randint(0, min(self._armor, 10))
            health_loss = max(damage - armor_loss, 0)
            self._armor -= armor_loss
            self._health -= health_loss
            print(f"{self.name} теряет {health_loss} здоровья и {armor_loss} брони")
        else:
            self._health -= damage
            print(f"{self.name} теряет {damage} здоровья")


        self._health = max(0, self._health)
        self._armor = max(0, self._armor)


def resolve_round(w1, w2):
    action1 = random.choice(["attack", "rest"])
    action2 = random.choice(["attack", "rest"])

    print(f"\n{w1.name} выбирает {action1}")
    print(f"{w2.name} выбирает {action2}")

    if action1 == "attack":
        damage = w1.attack()
        if action2 == "attack":
            damage2 = w2.attack()
            w1.take_damage(damage2)
            w2.take_damage(damage)
        else:  # w2 отдыхает
            w2.take_damage(damage)
            w2.recover_stamina()
    else:  # w1 отдыхает
        w1.recover_stamina()
        if action2 == "attack":
            damage2 = w2.attack()
            w1.take_damage(damage2)
        else:
            w2.recover_stamina()


# Создание воинов
warrior1 = Warrior("Геракл")
warrior2 = Warrior("Зевс")

round_num = 1
while warrior1.is_alive() and warrior2.is_alive():
    print(f"\n--- Раунд {round_num} ---")
    resolve_round(warrior1, warrior2)
    print(f"{warrior1.name}: HP={warrior1.health}, Armor={warrior1.armor}, Stamina={warrior1.stamina}")
    print(f"{warrior2.name}: HP={warrior2.health}, Armor={warrior2.armor}, Stamina={warrior2.stamina}")
    round_num += 1

print("\n--- Конец боя ---")
winner = warrior1 if warrior1.is_alive() else warrior2
print(f"Победил {winner.name}")
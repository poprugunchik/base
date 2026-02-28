import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 50
        self.stamina = 100

    def is_alive(self):
        return self.health > 0

    def attack(self):
        self.stamina -= 10
        print(f"{self.name} атакует!")

    def defend(self):
        print(f"{self.name} защищается!")

    #считаю, что по правилам игр, если оба соперника не атакуют, то выносливость должна все же пополняться
    def recover_stamina(self):
        self.stamina += 15
        print(f"{self.name} восстанавливает 15 выносливости")

    def defend_from_attack(self):
        if self.armor > 0:
            health_loss = random.randint(0, 20)
            armor_loss = random.randint(0, 10)
            self.health -= health_loss
            self.armor -= armor_loss
            print(f"{self.name} теряет {health_loss} здоровья и {armor_loss} брони")
        else:
            health_loss = random.randint(10, 30)
            self.health -= health_loss
            print(f"Броня сломана! {self.name} теряет {health_loss} здоровья")

    def take_full_damage(self):
        damage = random.randint(10, 30)
        self.health -= damage
        print(f"{self.name} теряет {damage} здоровья")

    def normalize(self):
        self.health = max(0, self.health)
        self.armor = max(0, self.armor)
        self.stamina = max(0, self.stamina)


warrior1 = Warrior("Геракл")
warrior2 = Warrior("Зевс")

round_num = 1

def resolve_round(w1, w2):
    action1 = random.choice(["attack", "defend"])
    action2 = random.choice(["attack", "defend"])

    print(f"\n{w1.name} выбирает {action1}")
    print(f"{w2.name} выбирает {action2}")

    # Оба атакуют
    if action1 == "attack" and action2 == "attack":
        w1.attack()
        w2.attack()
        w1.take_full_damage()
        w2.take_full_damage()

    elif action1 == "attack" and action2 == "defend":
        w1.attack()
        w2.defend()
        w2.defend_from_attack()

    elif action1 == "defend" and action2 == "attack":
        w2.attack()
        w1.defend()
        w1.defend_from_attack()

    else:
        w1.defend()
        w2.defend()
        w1.recover_stamina()
        w2.recover_stamina()

    w1.normalize()
    w2.normalize()


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
if warrior1.is_alive():
    print(f"Победил {warrior1.name}")
else:
    print(f"Победил {warrior2.name}")
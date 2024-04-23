class Hero:
    def __init__(self, name, hp, mp):
        self.name = name
        self.max_hp = 100
        self.max_mp = 200
        self.hp = min(hp, self.max_hp)
        self.mp = min(mp, self.max_mp)

    def take_damage(self, damage, attacker):
        if self.hp > 0:
            self.hp -= damage
            if self.hp <= 0:
                print(f"{self.name} has been killed by {attacker}!")
            else:
                print(f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hp} HP left!")

    def cast_spell(self, spell_name, mp_needed):
        if self.mp >= mp_needed:
            self.mp -= mp_needed
            print(f"{self.name} has successfully cast {spell_name} and now has {self.mp} MP!")
            return True
        else:
            print(f"{self.name} does not have enough MP to cast {spell_name}!")
            return False

    def recharge(self, amount):
        mp_before = self.mp
        self.mp = min(self.mp + amount, self.max_mp)
        amount_recovered = self.mp - mp_before
        print(f"{self.name} recharged for {amount_recovered} MP!")

    def heal(self, amount):
        hp_before = self.hp
        self.hp = min(self.hp + amount, self.max_hp)
        amount_recovered = self.hp - hp_before
        print(f"{self.name} healed for {amount_recovered} HP!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}\n  HP: {self.hp}\n  MP: {self.mp}"


n = int(input())
heroes = {}

for _ in range(n):
    name, hp, mp = input().split()
    hp, mp = int(hp), int(mp)
    heroes[name] = Hero(name, hp, mp)

while True:
    command = input()
    if command == "End":
        break

    action, *args = command.split(" - ")
    hero_name = args[0]

    if hero_name in heroes:
        hero = heroes[hero_name]
        if action == "TakeDamage":
            damage, attacker = int(args[1]), args[2]
            hero.take_damage(damage, attacker)
        elif action == "CastSpell":
            spell_name, mp_needed = args[2], int(args[1])
            hero.cast_spell(spell_name, mp_needed)
        elif action == "Recharge":
            amount = int(args[1])
            hero.recharge(amount)
        elif action == "Heal":
            amount = int(args[1])
            hero.heal(amount)

alive_heroes = [hero for hero in heroes.values() if hero.is_alive()]
for hero in alive_heroes:
    print(hero)
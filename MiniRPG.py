#player and enemy system

class Player:
    
    
    def __init__(self, name, health, atk):
        self.name = name
        self.__health = health
        self.atk = atk
        
    def get_hp(self):
        return self.__health
    
    def show_stats(self):
        print(f"""
Name: {self.name}
HP: {self.__health}
Attack: {self.atk}
""")
        
    def taking_damage(self, dmg):
        self.__health = max(0, self.__health - dmg)
    
    def is_aliveplayer(self):
        return self.__health > 0
        
    @staticmethod
    def hpvalid(self):
        return self.__health >= 0

    def is_alive(self):
        return self.__health > 0
#item system
class Item:
    def __init__(self, name):
        self.name = name
    
    def show_info(self, name):
        return "Name:", name
#weapon system    
class Weapon(Item):
    def __init__(self, name, dmg):
        super().__init__(name)
        self.dmg = dmg
        
    def show_info(self, name, dmg):
        print("Name:", name)
        print("Damage:", dmg)
        
#inventory system
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
#buff system
def applybuff(stat_change_func, player):
    return stat_change_func(player)

def hp_buff(player):
    player._Player__health += 20
    return player

#combat system
def attack(attacker, defender):
    try:
        if not defender.is_alive():
            raise ValueError("Target already defeated")
        
        defender.taking_damage(attacker.atk)
        print(f"{attacker.name} attacks {defender.name}")
        
    except ValueError as e:
        print("Error", e)
        
    else:
        print(f"{defender.name} HP:", defender.get_hp())
        
    finally:
        print("Attack attempt finished.\n")
        
#game flow
options = [1, 2, 3, 4 ,5]
optionuser = 0
players = []
weapons = []
while True:
    print("Welcome to Luki's mini RPG game!")
    print()
    print("1. Create player or enemy\n")
    print("2. Weapon\n")
    print("3. Attack an enemy\n")
    print("4. Show Player or enemy stats\n")
    print("5. Exit")
    
    optionuser = int(input("Enter an option:"))
    if optionuser == options[0]:
        name = input("Enter player or enemy name: ")
        try:
            hp = int(input("Enter the hp:"))
            if hp == type(str):
                raise ValueError
        except ValueError:
            print("Enter an appropriate value.")
            
        try:
            atk = int(input("Enter attack power: "))
            if atk == type(str):
                raise ValueError
        except ValueError:
            print("Enter an appropriate value.")
        player = Player(name, hp, atk)
        players.append(player)
        print(f"{name} created!") 
        
    elif optionuser == options[1]:
        name = input("Enter your weapon's name:")
        try:
            atk = int(input("Enter the attack damage:"))
        except ValueError:
             print("Enter an appropriate value.")
        weapon = Weapon(name, atk)
        weapons.append(weapon)
        print(f"{name} created!")
        
    elif optionuser == options[2]:
        if len(players) < 2:
            print("Need at least 2 players to attack.")
        else:
            attack(players[0], (players[1]))
            
    elif optionuser == options[3]:
        if len(players) == 0:
            print("No player created.")
        else:
            for player in players:
                player.show_stats()
            
    elif optionuser == options[4]:
        quit()
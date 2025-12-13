class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class Weapon(Item):
    def __init__(self, name, price, damage, wtype):
        super().__init__(name, price)
        self.damage = damage
        self.wtype = wtype
        
    def info(self):
        print(f"name: {self.name}, type: {self.wtype}, dmg: {self.damage}, price: {self.price}")

sword = Weapon("Sword", "10 Coins", "2 Damage", "Melee")
sword.info()


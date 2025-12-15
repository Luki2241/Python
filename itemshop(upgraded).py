class Item:
    def __init__(self, name, price):
        self.name = name
        self.__price = price
        
    def get_price(self):
        return self.__price    
class Weapon(Item):
    def __init__(self, name, __price, damage, wtype):
        super().__init__(name, __price)
        self.damage = damage
        self.wtype = wtype
        
    def info(self):
        print(f"name: {self.name}, type: {self.wtype}, dmg: {self.damage},")
        

sword = Weapon("Sword", "10 Coins", "2 Damage", "Melee")
sword.info()
print("price:", sword.get_price())

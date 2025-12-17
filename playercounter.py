class Player:
    total_players = 0
    
    def __init__(self, name):
        self.name = name
        Player.total_players += 1
        
    @classmethod    
    def show_playercount(cls):
        print("Total players:", cls.total_players)
        
p1 = Player("Bob")
p2 = Player("Quandale Dingle")

Player.show_playercount()
    
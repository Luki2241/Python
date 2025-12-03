player = {"hp": 100, "atk": 10}

def applybuff(stat_change_func, player):
    return stat_change_func(player)

hp = lambda hpbuff: {"hp": hpbuff["hp"] + 20, "atk": hpbuff["atk"]}

atk = lambda atkbuff: {"atk": atkbuff["atk"] + 10, "hp": atkbuff["hp"]}

player = applybuff(hp, player)

print(player)
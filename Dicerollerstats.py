import random

rolls = []
for i in range(20):
    rolls.append(random.randint(1, 6))
    
print("Highest roll:", max(rolls))
print()
print("Lowest roll:", min(rolls))
print()
print("How many 1s:", rolls.count(1))
print()    
print("How many 2s:", rolls.count(2))
print()
print("How many 3s:", rolls.count(3))
print()
print("How many 4s:", rolls.count(4))
print()
print("How many 5s:", rolls.count(5))
print()
print("How many 6s:", rolls.count(6))
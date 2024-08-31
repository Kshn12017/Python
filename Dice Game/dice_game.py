import random

no_of_remaning_chance = 0
print("Dice Rolling Game\n")

print("Start Game")
print("Number of Chances to be played")
n=input()

while no_of_remaning_chance<int(n):
    input("Roll dice(press any key): ")
    
    no_of_remaning_chance = no_of_remaning_chance + 1
    
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    
    print(d1,d2)
    
    if d1==d2:
        print("You WIN\n")
        break
    else:
        print("You LOSE")
    print(f"{int(n) - no_of_remaning_chance} chance left out of {int(n)}\n")
print("Game Over")
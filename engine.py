#Revolver Case Skins
import random as rand
import RevolverCase as RC

x = 0


def get_skin_revolver_case():
    number = (rand.randint(1, 10000)) / 100
    if number <= 0.26:
        rarity = "Gold"
    elif number <= 0.64:
        rarity = "Red"
    elif number <= 3.2:
        rarity = "Pink"
    elif number <= 15.98:
        rarity = "Purple"
    else:
        rarity = "Dark Blue"
    
    return rand.choice(RC.skins_list[rarity])


while x < 10:
    print(get_skin_revolver_case())
    x += 1

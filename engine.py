#Revolver Case Skins
import random as rand
import RevolverCase as RC



def get_skin_case():
    number = (rand.randint(1, 10000)) / 100
    if number <= 0.26:
        rarity = "Gold"
        float = rand.randint(1, 20000000) / 100000000
    elif number <= 0.64:
        rarity = "Red"
        float = rand.randint(1, 30000000) / 100000000
    elif number <= 3.2:
        rarity = "Pink"
        float = rand.randint(1, 45000000) / 100000000
    elif number <= 15.98:
        rarity = "Purple"
        float = rand.randint(1, 65000000) / 100000000
    else:
        rarity = "Dark Blue"
        float = rand.randint(1, 90000000) / 100000000
    
    StatTrack = rand.randint(0,9)
    if StatTrack == 0:
        StatTrack = "StatTrack"
    else: 
        StatTrack = ""
       
    return rand.choice(RC.skins_list[rarity]), float, StatTrack

skin, float_value, StatTrack = get_skin_case()
print(f"Skin: {StatTrack} {skin}, Float value: {float_value}")

 

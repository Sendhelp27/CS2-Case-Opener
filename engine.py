#Revolver Case Skins
import random as rand

x = 0

skins_list = {
    "Gold": ["Bayonet|", "Flip Knife|", "Gut Knife|", "Karambit|", "M9 Bayonet|"],
    "Red": ["M4A4 | Royal Paladin", "R8 Revolver | Fade"],
    "Pink": ["AK-47 | Point Disarray", "G3SG1 | The Executioner", "P90 | Shapewood"],
    "Purple": ["PP-Bizon| Fuel Rod", "Five-SeveN | Retrobution", "Negev | Power Loader", "SG 553 | Tiger Moth", "Tec-9 | Avalanche", "XM1014 | Teclu Burner"],
    "Dark Blue": ["R8|Revolver", "AUG| Richochet", "Desert Eagle| Corinthian", "P2000| Imperial", "Sawed-Off| Yorick", "SCAR-20| Outbreak"]
}

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
    
    return rand.choice(skins_list[rarity])


while x < 10:
    print(get_skin_revolver_case())
    x += 1

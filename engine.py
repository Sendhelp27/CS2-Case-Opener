#Revolver Case Skins
import random as rand


skins_rarity = ["Gold", "Red", "Pink", "Purple", "Dark Blue"]
skins_weighting = [0.26, 0.38, 2.34, 15.98, 79.92]
skins_list = {
    "Gold": ["Bayonet|", "Flip Knife|", "Gut Knife|", "Karambit|", "M9 Bayonet|"],
    "Red": ["M4A4 | Royal Paladin", "R8 Revolver | Fade"],
    "Pink": ["AK-47 | Point Disarray", "G3SG1 | The Executioner", "P90 | Shapewood"],
    "Purple": ["PP-Bizon| Fuel Rod", "Five-SeveN | Retrobution", "Negev | Power Loader", "SG 553 | Tiger Moth", "Tec-9 | Avalanche", "XM1014 | Teclu Burner"],
    "Dark Blue": ["R8|Revolver", "AUG| Richochet", "Desert Eagle| Corinthian", "P2000| Imperial", "Sawed-Off| Yorick", "SCAR-20| Outbreak"]
}

    
def get_skin_rarity_revolver_case():
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

print(get_skin_rarity_revolver_case())

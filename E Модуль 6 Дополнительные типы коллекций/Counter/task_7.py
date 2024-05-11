from collections import Counter

witcher_inventory = Counter(doppler_trophy=1, alcohest=10, mahakaman_spirit=10,
                            siren_vocal_cords=3, ghouls_blood=4)

losses = dict(ducat=10, alcohest=20, mahakaman_spirit=5, ghouls_blood=4)

witcher_inventory.subtract(losses)

print(witcher_inventory)

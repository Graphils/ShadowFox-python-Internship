justice_league = ["Superman", " Batman", "Wonder woman", "Flash", "Aquaman", "Green lantern"]

# calculate the number of members in the justice league
print(len(justice_league))

# Batman recruited Batgirl and Nightwing as new members. add them to list
justice_league.extend(["Batgirl", "Nightwing"])
print(justice_league)

# Wonder woman is now the leader of the justice league. Move her to the beginning the lisr
justice_league.remove("Wonder woman")
justice_league.insert(0, "Wonder woman")
print(justice_league)

# Aquaman and Batman are having conflicts. Move Green lantern in between them
justice_league.remove("Green lantern")
justice_league.insert(3,"Green lantern")
print(justice_league)

# Superman assembles a new team due to crises
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Maritain Manhunter", "Green Arrow"]
print(justice_league)

# sort the justice league alphabetically . The hero at the 0th index will become the leader.
justice_league.sort()
print(justice_league)
print(justice_league[0])

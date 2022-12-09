friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# .difference() calculates the different values between two sets
local_friends = friends.difference(abroad)
print(f"Only Local Friends: {local_friends}")

# Empty set calculation
local_friends2 = abroad.difference(friends)
print(f"Empty Set: {local_friends2}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ adding total friends into a set using .union()
local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print(f"All Friends: {friends}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ pull values that are in both sets using .intersection()
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
art_only = art.difference(science)
science_only = science.difference(art)

print(f"Who studies both subjects? {both}")
print(f"Only Art: {art_only}")
print(f"Only Science: {science_only}")


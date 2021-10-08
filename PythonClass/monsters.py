zombies = {"No emotions", "Taste for Flesh", "Death To Humans"}

aliens = {"Taste for Flesh", "Advanced Technoloy", "Death To Humans"}

robots = {"Advanced Technoloy", "No emotions", "Death To Humans"}

print("Zombies and Aliens:", zombies.intersection(aliens))

print("Robots and Aliens:", robots.intersection(aliens))

print("All three:", zombies.intersection(aliens, robots))


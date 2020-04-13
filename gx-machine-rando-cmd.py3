import random

machines = {"Astro Robin", "Big Fang", "Black Bull", "Blood Hawk", "Blue Falcon", "Bunny Flash", "Cosmic Dolphin", "Crazy Bear", "Dark Schneider", "Death Anchor", "Deep Claw", "Fat Shark", "Fire Stingray", "Golden Fox", "Great Star", "Green Panther", "Groovy Taxi", "Hyper Speeder", "Iron Tiger", "King Meteor", "Little Wyvern", "Mad Wolf", "Magic Seagull", "Mighty Hurricane", "Mighty Typhoon", "Night Thunder", "Pink Spider", "Queen Meteor", "Rainbow Phoenix", "Red Gazelle", "Rolling Turtle", "Silver Rat", "Sonic Phantom", "Space Angler", "Spark Moon", "Super Piranha", "Twin Noritta", "White Cat", "Wild Boar", "Wild Goose", "Wonder Wasp"}

tracks = ["Twist Road", "Split Oval", "Surface Slide", "Loop Cross", "Multiplex",
          "Drift Highway", "Aero Dive", "Mobius Ring", "Long Pipe", "Serial Gaps",
          "Cylinder Knot", "Intersection", "Double Branches", "Half Pipe", "Ordeal",
          "Trident", "Lateral Shift", "Undulation", "Dragon Slope", "Slim-line Slits",
          "Screw Drive", "Meteor Stream", "Cylinder Wave", "Thunder Road", "Spiral", "Sonic Oval"]

current_index = 0
mulligans = 0
run = random.sample(machines, 26)
leftovers = machines - set(run)
print("Press enter to go to the next track\n"
      "Type \"r\" to reset\n"
      "Type \"p\" to go back to the previous track\n"
      "Type \"m\" to use a mulligan\n")

while(1):
    if current_index < 26:
        print("Current track: " + tracks[current_index] + "\n" + "Current machine: " + run[current_index])
    else:
        print("Run finished with " + str(mulligans) + " mulligan(s), please reset!")

    command = input().lower()
    if command == "" or command == "n":
        if current_index < 26:
            current_index += 1
    elif command == "reset" or command == "r":
        run = random.sample(machines, 26)
        leftovers = random.sample((machines - set(run)), 15)
        current_index = 0
        mulligans = 0
        print("New run started\n")
    elif command == "previous" or command == "p":
        if current_index > 0:
            current_index -= 1
        else:
            print("Can't go back further!")
    elif command == "mulligan" or command == "m":
        if (leftovers):
            run[current_index] = leftovers.pop()
            mulligans += 1
            print("You have used " + str(mulligans) + " mulligan(s)!")
        else:
            print("No mulligans left!")

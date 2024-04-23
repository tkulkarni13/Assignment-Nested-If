# Task 1: Code Correction

place = input("Choose a place: forest or cave?\n")
if (place == "forest"): # user picks forest
    action = input("climb a tree or cross a river\n")
    if (action == "climb a tree"):
        print("You found a bird's nest")
    elif (action == "cross a river"):
        print("You found a boat")
    else:
        pass
elif (place == "cave"): # user pick cave
    action = input("light a torch or proceed in the dark\n")
    if (action == "light a torch"):
        print("You spotted treasure deeper in the cave")
    elif (action == "proceed in the dark"):
        print("You accidently bump your head with no vision")
    else:
        pass
else:
    pass

# Task 2: Setting the Scene
# Shown above starting at line 11.

# Task 3: Default Path
# Pass statements added to conditionals. Additional choices can be given to player in the future.
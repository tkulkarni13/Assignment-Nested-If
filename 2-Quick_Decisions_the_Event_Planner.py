# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue Selection

audio_system = "big speaker" if attendees > 100 else "small speaker"
projector = "big screen" if attendees > 100 else "small screen"
print(audio_system)
print(projector + "\n")

# Task 3: Catering Choices

food = input("Do you want vegetarian food?\n")
print("I recommend Veggie Delight Caterers then.") if food == "yes" else print("I recommend Gourmet Meals Caterers then.")
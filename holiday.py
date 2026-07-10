# Holiday Activity Planner

holiday = input("What type of holiday do you like? (Beach/Mountains): ").lower()

if holiday == "beach":
    activity = input("Do you like adventure or relaxation? ").lower()

    if activity == "adventure":
        print("Your holiday plan: Try surfing, snorkeling, and beach volleyball!")
    else:
        print("Your holiday plan: Relax on the beach, read a book, and enjoy the sunset.")

elif holiday == "mountains":
    activity = input("Do you like hiking or camping? ").lower()

    if activity == "hiking":
        print("Your holiday plan: Explore scenic trails and enjoy breathtaking views!")
    else:
        print("Your holiday plan: Camp under the stars and enjoy a cozy bonfire.")

else:
    print("Sorry, please choose either Beach or Mountains.")
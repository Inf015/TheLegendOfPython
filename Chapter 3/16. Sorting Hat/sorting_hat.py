# Write code below 💖


gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0


print("Q1) Do you like Dawn or Dusk?")
print("  1) Dawn")
print("  2) Dusk")
answer = int(input("Your answer: "))

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

print("\nQ2) When I’m dead, I want people to remember me as:")
print("  1) The Good")
print("  2) The Great")
print("  3) The Wise")
print("  4) The Bold")
answer = int(input("Your answer: "))

if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print("Wrong input.")

# Q3
print("\nQ3) Which kind of instrument most pleases your ear?")
print("  1) The violin")
print("  2) The trumpet")
print("  3) The piano")
print("  4) The drum")
answer = int(input("Your answer: "))

if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print("Wrong input.")

# Print scores
print("\nScores:")
print("Gryffindor:", gryffindor)
print("Ravenclaw:", ravenclaw)
print("Hufflepuff:", hufflepuff)
print("Slytherin:", slytherin)

houses = {
    "Gryffindor": gryffindor,
    "Ravenclaw": ravenclaw,
    "Hufflepuff": hufflepuff,
    "Slytherin": slytherin
}

max_score = max(houses.values())
winners = [house for house, score in houses.items() if score == max_score]

if len(winners) == 1:
    print("\nThe Sorting Hat has made its decision! You belong to", winners[0] + "!")
else:
    print("\nIt's a tie between:", ", ".join(winners) + "!")

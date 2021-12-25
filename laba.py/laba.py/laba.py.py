import random

print("""Choose:)
0. scissors
1. rock
2. paper  """)
numOfChoice = int(input())
computerChoice = ["scissors", "rock", "paper"]
x = random.randint(0, 2)
print("Your chose", computerChoice[numOfChoice])
print("The computer chose", computerChoice[x])
if numOfChoice <= -1 or numOfChoice >= 3:
    print("Clever, huh???")
if x == numOfChoice:
    print("Draw")
if x == 0 and numOfChoice == 1:
    print("You won ")
if x == 0 and numOfChoice == 2:
    print("You lost ")
if x == 1 and numOfChoice == 2:
    print("You won  ")
if x == 1 and numOfChoice == 0:
    print("You lost ")
if x == 2 and numOfChoice == 1:
    print("You lost ")
if x == 2 and numOfChoice == 0:
    print("You won ")

raw = open('inputs/day2.txt').read()
rounds = raw.split("\n")
score = 0

for round in rounds:
    if round == "A X":
        score += 1 + 3
    elif round =="A Y":
        score += 2 + 6
    elif round == "A Z":
        score += 3 + 0
    elif round == "B X":
        score += 1 + 0
    elif round =="B Y":
        score += 2 + 3
    elif round == "B Z":
        score += 3 + 6
    elif round == "C X":
        score += 1 + 6
    elif round =="C Y":
        score += 2 + 0
    elif round == "C Z":
        score += 3 + 3

print("First task: ", score)

score = 0
for round in rounds:
    if round == "A X":
        score += 3 + 0
    elif round =="A Y":
        score += 1 + 3
    elif round == "A Z":
        score += 2 + 6
    elif round == "B X":
        score += 1 + 0
    elif round =="B Y":
        score += 2 + 3
    elif round == "B Z":
        score += 3 + 6
    elif round == "C X":
        score += 2 + 0
    elif round =="C Y":
        score += 3 + 3
    elif round == "C Z":
        score += 1 + 6
print("Second task: ", score)
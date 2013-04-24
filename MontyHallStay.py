import random

def CreateProblem(nDoors):
    p = [ "tiger" ] * nDoors
    p[random.randint(0, len(p)-1)] = "princess"
    return p

def KingOpensDoor(s, playerChoice):
    for i in range(len(s)):
        if s[i] != "princess" and i != playerChoice:
            return i

def PlayerChange(s, kingOpen, playerChoice):
    for i in range(len(s)):
        if i != kingOpen and i != playerChoice:
            return i

def MontyHallStay(N, nDoors):
    s = 0
    f = 0
    for i in range(N):
        p = CreateProblem(nDoors)
        playerChoice = random.randint(0, nDoors-1)
        king_opens = KingOpensDoor(p, playerChoice)

        if p[playerChoice] == "princess":
            s += 1
        else:
            f += 1
    return (s, f)

def MontyHallChange(N, nDoors):
    s = 0
    f = 0
    for i in range(N):
        p = CreateProblem(nDoors)
        playerChoice = random.randint(0, nDoors-1)
        kingOpen = KingOpensDoor(p, playerChoice)
        playerChoice = PlayerChange(p, kingOpen, playerChoice);

        if p[playerChoice] == "princess":
            s += 1
        else:
            f += 1
    return (s, f)

def MontyHallRandom(N, nDoors):
    s = 0
    f = 0
    for i in range(N):
        p = CreateProblem(nDoors)
        playerChoice = random.randint(0, nDoors-1)
        kingOpen = KingOpensDoor(p, playerChoice)
        if random.randint(0, 1):
            playerChoice = PlayerChange(p, kingOpen, playerChoice);

        if p[playerChoice] == "princess":
            s += 1
        else:
            f += 1
    return (s, f)


def main():
    runTimes = 100000;
    nDoors = 100;
    (s, f) = MontyHallStay(runTimes, nDoors)
    print("Stay:", "Sucesss", s, "Failure", f)
    (s, f) = MontyHallChange(runTimes, nDoors)
    print("Change:", "Sucesss", s, "Failure", f)
    (s, f) = MontyHallRandom(runTimes, nDoors)
    print("Random:", "Sucesss", s, "Failure", f)

if __name__ == "__main__":
    main()

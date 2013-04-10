puzzle1 = [[ "_", "_", "_", "_", "_", "_"],
           [ "_", "P", "_", "_", "_", "_"],
           [ "_", "_", "_", "_", "_", "_"]]

def PrintPuzzle(puzzle):
    x = len(puzzle)
    y = len(puzzle[0])
    print("---" * y)
    for i in range(x):
        print("|", end= "")
        for j in range(y):
            print(puzzle[i][j], "", end="")
        print("|")
    print("---" * y)
        
PrintPuzzle(puzzle1)

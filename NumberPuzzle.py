def NumberPuzzle(o_puzzle):
    print("The input puzzle is " + o_puzzle)
    puzzle = o_puzzle
#    while( eval(puzzle) == False ):
    for i in range(len(puzzle)):
        if puzzle != "=":
            for j in "0123456789+-*/ ":
                puzzle = o_puzzle[0:i] + j + o_puzzle[i+1:]
                try:
                    if eval( puzzle ):
                        print(puzzle)
                except SyntaxError:
                    pass
                    #print("Illegal puzzle")
    #return puzzle

def main():
    NumberPuzzle("77+3==70")

if __name__ == "__main__":
    main()

def Triangle(slist):
    pass

def MagicTriangle():
    sol = []
    for i in range(1, 9, 1):



    return sol

def PrintMagicTriangle(p):
    print("Solution")
    print("{0:3d}".format(p[6]))
    print("{0:3d}{1:3d}".format(p[4], p[7]))
    print("{0:3d}   {1:3d}".format(p[4], p[8]))
    print("{0:3d}{1:3d}{2:3d}{3:3d}".format(p[0], p[1], p[2], p[3]))
    print("")

x = MagicTriangle()

if x != None:
    for s in x:
        PrintMagicTriangle(s)
    print("Number of solutions ", len(x))

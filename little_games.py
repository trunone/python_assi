#!/usr/bin/env python3
import sys

def fizzbuzz(N):
    for i in range(1,N):
        if i%3 == 0 and i%5 == 0:
            print('fizzbuzz')
        elif i%3 == 0:
            print('fizz')
        elif i%5 == 0:
            print('buzz')
        else:
            print(i)

def sumfizzbuzz(N):
    tmp = 0
    for i in range(1, N):
        if i%3 == 0 and i%5 == 0:
            tmp += i
        elif i%3 == 0:
            tmp += i
        elif i%5 == 0:
            tmp += i
    return tmp

def Maximum(l):
    tmp = None
    if l == []:
        err = "Error"
    else:
        err = "Ok"
        tmp = l[0]
    for i in l:
        if i > tmp:
            tmp = i
    return (err, tmp)

list = [(0, 3), 12, 34, ['a', 'b']]

def reverse(list):
    s = ""
    for i in range(len(list)-1, -1, -1):
        s += list[i]
    return s

def reverse3(list):
    if list == "":
        return ""
    else:
        return reverse3(list[1:]) + list[0]

def printMultiplicationTalbe(N):
    print(" " * 4, end="")
    for i in range(1,N+1):
        print("{0:4d}".format(i), end="")
    print("")
    for i in range(1,N+1):
        print("{0:4d}".format(i), end="")
        for j in range(1, N+1):
            if j <= i:
                print("{0:4d}".format(i*j), end="")
        print("")

def main():
    print(sys.version)
#    fizzbuzz(100)
#    print(sumfizzbuzz(100))

#    e, v = Maximum([1, 5, -9, -8, 7, 4, 3])
#    print("e=", e, "v=", v)
#    e, v = Maximum([])
#    print("e=", e, "v=", v)

    print(reverse("this is a test."))
#    print(list)
#    print(reverse3(list))
    print(reverse3("this is a test."))
#    printMultiplicationTalbe(9)

if __name__ == "__main__":
    main()

##s = "Python is great"
##print(s[3])
##print(s[6:])
##print(s[0:4])
##print(s[0:3]+s[4:len(s)])
##print(s[4:-1])
##print(s[-3:-1])
##print(s[-1:-3])

##def max2(list):
##    list.remove(max(list))
##    return max(list)
##
##print(max2([1, 2, 3, 4, 5]))
##print(max2([1,2,3,3]))
##print(max2([3,4,2,3,5]))

##print([x*(2 - x%2) for x in [2, 3, 4, 5, 6, 7, 8]])

##def func(list):
##    print(list)
##    if(list != []):
##        if(list[0]%2 != 0):
##            return func(list[1:]) + [list[0]]
##        else:
##            return func(list[1:])
##    return []
##
##print("func([1, 2, 3, 4, 5])","->", func([1,2,3,4,5]))

##def func(list, x):
##    sum = 0
##    ind = -1
##    for i in range(0, len(list)):
##        if(list[i] > x):
##            ind = i
##            break
##
##    for i in range(ind, len(list)):
##        sum += list[i]
##
##    return sum
##
##print(func([1,2,3,3,2,1,4,5,6], 3))
##print(func([2,3,1,4,5,6], 2))
##print(func([2,3,1,4,5,6], 0))

def isSquared(x):
    flag = False
    for i in range(1, int(x/2)):
        if(((x - (i**2))**.5) - int((x - (i**2))**.5) == 0):
            flag = True
            break
    return flag

print(isSquared(25))
print(isSquared(10))
print(isSquared(7))

##sum = 1
##for i in range(16, 0, -1):
##    sum *= i
##print(sum)

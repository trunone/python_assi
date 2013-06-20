
## Question 1
#count = 0

#def func(x):
#    global count
#    if(x<2):
#        r = 1
#        count += 1
#    else:
#        r = func(x-1)*2 + func(x-2)
#        count += 5
#    return r
## Qestion 2
#def func(x):
#    global count
#    a = [0.0] * (x+1)
#    a[0] = 1.0
#    a[1] = 1.0
#    count += x+3
#
#    for i in range(2, x+1):
#        a[i] = a[i-1]*2 + a[i-2]
#        count += 5
#
#    return a[x]
#
#print("func(5)", func(5))
#print(count)

##Qestion 3
#def ReplaceWithVowels(s):
#    slist = list(s)
#    for i in range(len(slist)):
#        if slist[i] in ('a', 'e', 'i', 'o', 'u'):
#            if((i-1)>=0):
#                slist[i-1] = slist[i]
#    return "".join(slist)
#
#print(ReplaceWithVowels('bcega'))
#print(ReplaceWithVowels('bceai'))
#print(ReplaceWithVowels('abcdef'))
#print(ReplaceWithVowels('a'))
#print(ReplaceWithVowels('b'))

def CrossProduct(list1, list2):
    olist = []
    for i in list1:
        for j in list2:
            olist.append((i, j))
    return olist

print(CrossProduct([1, 2, 3], [4, 5]))
print(CrossProduct([1, 2, 3], []))
print(CrossProduct([6], [1, 2, 3]))

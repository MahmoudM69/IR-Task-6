from numpy.lib.scimath import sqrt
from math import floor
from operator import itemgetter


_to = [[1, 9, [2, 4, 8, 16, 19, 23, 28, 41, 43]],
       [2, 6, [3, 5, 7, 21, 51, 78]]]

_to.sort(key=itemgetter(0))
for i in range(len(_to)):
    _to[i][2].sort()


_be = [[1, 8, [1, 2, 3, 5, 7, 42, 51, 60]],
       [2, 7, [8, 18, 19, 27, 29, 50, 77]]]

_be.sort(key=itemgetter(0))
for i in range(len(_be)):
    _be[i][2].sort()


answer = []


def checker(l1, l2):
    l1i = 0
    l2i = 0
    while(l1i < len(l1) and l2i < len(l2)):
        if(l1[l1i] == l2[l2i]+1):
            answer.append([l2[l2i], l1[l1i]])
            l1i += 1
            l2i += 1
        elif(l1[l1i] < l2[l2i] and l1i < len(l1)):
            l1i += 1
        elif (l2[l2i] < l1[l1i] and l2i < len(l2)):
            l2i += 1

    print(answer)


def samelist(f, s):
    i = 0
    x = 0
    while i < len(f) and x < len(s):
        if f[i][0] == s[x][0]:
            print("Document # {0} :".format(f[i][0]))
            checker(f[i][2], s[x][2])
            i += 1
            x += 1
        elif f[i][0] < s[x][0]:
            i += 1
        else:
            x += 1


samelist(_to, _be)

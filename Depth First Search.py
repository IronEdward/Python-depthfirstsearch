import sys

print "Enter the number of inputs you want: [Example: X --> Y]"
InputNum = int(raw_input())
array = dict()
for i in xrange(0, InputNum):
    a = raw_input().split()
    first = a[0]; second = a[2]
    if(i == 0):
        b = first
    if(first in array and second in array[first]):
        continue
    array.setdefault(first, [])
    array[first].append(second)
    array.setdefault(second, [])
    array[second].append(first)

print "What do you want to find?"
letter = raw_input()
if(letter not in array):
    print "%s does not exist in graph. Exiting..." % (letter)
    sys.exit()

print array
checker = list()

def DFS(Cnode):
    checker.append(Cnode)
    #print Cnode
    if(Cnode == letter):
        print "Found %s." % (letter)
        sys.exit()
    length = len(array[Cnode])
    for j in xrange(0, length):
        if(array[Cnode][j] not in checker):
            DFS(array[Cnode][j])

DFS(b)

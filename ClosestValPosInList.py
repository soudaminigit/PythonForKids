# Given List, and an integer X,
# Find the closest value Position for X in the list


def FindClosest(mylist, x):
    pos = 0
    diff = ""
    for i, num in enumerate(myList):
        if abs(x - num) < diff:
            diff = abs(x - num)
            pos = i
    return pos

mylist = [10, 2, 8, -5, 4, -5]
length = len(mylist)
x = -4
pos = FindClosest(mylist, x)
print("Closest Value Position "+str(pos))
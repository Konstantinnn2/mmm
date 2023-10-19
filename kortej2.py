R = 0
F = -1
def slicer(u, g):
    ftt = edf = R   
    if g in u:
        ftt = u.index(g)
    if u.count(g) > 1:
        edf = u.index(g, ftt + 1) + 1
    else:
        edf = F
    return u[ftt:edf]
print(slicer((3, 5, 6), 7))
print(slicer((2, 3, 5, 4, 3, 3, 7, 8), 3))
print(slicer((1, 2, 6, 4, 1, 2, 7), 6))

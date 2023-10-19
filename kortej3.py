def sieve(iuy):
    g = []
    [g.append(item) for item in reversed(iuy) if item not in g]
    return tuple(g)
print(sieve([3, 5, 6, 7, 5,9]))
print(sieve([1, 2, 4, 2, 1, 6, 6, 8, 1, 9, 9]))
print(sieve((2, 1, 4, 3, 6, 5, 8, 7, 9.1)))

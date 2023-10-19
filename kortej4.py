def del_from_tuple(wer, u):
    mdb = list(wer)
    if u in wer:
        mdb.remove(u)
    return tuple(mdb)
print(del_from_tuple((3, 4, 6), 3))
print(del_from_tuple((2, 5, 3, 6), 3))
print(del_from_tuple((1, 3, 5, 7, 8), 7))

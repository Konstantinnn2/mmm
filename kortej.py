def tpl_sort(abv):
    for element in abv:
        if not isinstance(element, int):
            return ()
        return tuple(sorted(abv))
print(tpl_sort((2, 5, 1.2, 6, 9)))
print(tpl_sort((3, 1, 2.2, 8, 7)))

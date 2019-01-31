# Algorytm of simple linear sorting
def qsort(items):
    if items:
        return qsort([x for x in items if x < items[0]]) + \
               [x for x in items if x == items[0]] + \
               qsort([x for x in items if x > items[0]])
    return []

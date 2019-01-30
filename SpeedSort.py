# Быстрая сортировка Хоара
import random as rnd


def quicksort(items, first, last):
    if first >= last: return

    i, j = first, last
    pivot = items[(last - first) // 2]
    while i <= j:
        while items[i] < pivot: i += 1
        while items[j] > pivot: j -= 1
        if i <= j:
            items[i], items[j] = items[j], items[i]
            i, j = i + 1, j - 1
            quicksort(items, first, j)
            quicksort(items, i, last)


items = [rnd.randint(1, 10) for _ in range(10)]
print(items)
quicksort(items, 0, len(items) - 1)
print(items)
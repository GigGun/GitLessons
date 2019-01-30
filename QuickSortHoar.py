# Быстрая сортировка Хоара
def quicksort(items):
    def sort(items, first, last):
        if first >= last: return

        i, j = first, last
        pivot = items[(last - first) // 2]
        while i <= j:
            while items[i] < pivot: i += 1
            while items[j] > pivot: j -= 1
            if i <= j:
                items[i], items[j] = items[j], items[i]
                i, j = i + 1, j - 1
                sort(items, first, j)
                sort(items, i, last)
        return items
    return sort(list(items), 0, len(items) - 1)

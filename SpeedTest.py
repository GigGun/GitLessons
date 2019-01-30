from datetime import datetime
import random as rnd
import QuickSortHoar
import BubbleSort

count = 100
items = [rnd.randint(0, count) for _ in range(count)]
print(items)
start = datetime.now()
QuickSortHoar.quicksort(items, 0, len(items) - 1)
end = datetime.now()
print(items)
delta = end - start
print(delta.seconds * 1000000 + delta.microseconds)

items = [rnd.randint(0, count) for _ in range(count)]
print(items)
start = datetime.now()
print(BubbleSort.bubblesort(items))
end = datetime.now()
delta = end - start
print(delta.seconds * 1000000 + delta.microseconds)


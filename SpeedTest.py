from datetime import datetime
import random as rnd
import QuickSortHoar

count = 100
items = [rnd.randint(0, count) for _ in range(count)]
print(items)
start = datetime.now()
QuickSortHoar.quicksort(items, 0, len(items) - 1)
end = datetime.now()
print(items)
print(end - start)

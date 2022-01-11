import heapq

# ascending heap sort
def heap_sort_as(iter):
    h = []
    result = []
    for value in iter:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# descending heap sort
def heap_sort_des(iter):
    h = []
    result = []
    for value in iter:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result
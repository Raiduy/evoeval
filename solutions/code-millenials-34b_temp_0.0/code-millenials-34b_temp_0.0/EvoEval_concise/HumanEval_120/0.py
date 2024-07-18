
def maximum(arr, k):
    pq = arr[:k]
    pq.sort()
    for num in arr[k:]:
        if num > pq[0]:
            pq.remove(min(pq))
            pq.append(num)
            pq.sort()
    return pq
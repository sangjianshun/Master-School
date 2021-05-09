def heapAdjust(L, i, j):
    next = i * 2
    tmp = L[i]
    while next <= j:
        if next + 1 <= j and L[next + 1] > L[next]:
            next = next + 1
        if L[next] > L[i]:
            L[i] = L[next]
            i = next
            next = next * 2
        else: break
    L[i] = tmp


def heapSort(L):
    L.insert(0, 0)
    for i in range(int((len(L) - 1) / 2), 0, -1):
        heapAdjust(L, i, len(L) - 1)
    for i in range(len(L) - 1, 0, -1):
        L[1], L[i] = L[i], L[1]
        heapAdjust(L, 1, i - 1)
    return L[1:]

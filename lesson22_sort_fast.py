def ArrayChunk(array):
    mid = array[len(array) // 2]
    left = 0
    right = len(array) - 1

    while left <= right:
        while array[left] < mid:
            left += 1

        while array[right] > mid:
            right -= 1

        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    return len(array) // 2


def sort_fast(m, left, right):
    if left >= right:
        return
    i1 = left
    i2 = right
    n = m[right]

    while i1 <= i2:
        while m[i1] < n:
            i1 += 1
        while m[i2] > n:
            i2 -= 1

        if i1 <= i2:
            m[i1], m[i2] = m[i2], m[i1]
            i1 += 1
            i2 -= 1
    sort_fast(m, left, i2)
    sort_fast(m, i1, right)

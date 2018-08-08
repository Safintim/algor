def sort_fast(m, left, right):
    i1 = left
    i2 = right
    n = m[right]

    while i1 != (i2 - 1):

        if m[i1] <= n:
            i1 += 1
            continue
        elif n <= m[i2]:
            i2 -= 1
            continue
        elif m[i1] > n > m[i2]:
            m[i1], m[i2] = m[i2], m[i1]

    if m[i1] < n:
        sort_fast(m, left, i2 - 1)
    if m[i2] > n:
        sort_fast(m, i2 + 1, right)
    # return m, i1, i2


n3 = [8, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 8, 8]
print(sort_fast(n3, 0, len(n3)-1))
print(n3)
# def sort_fast(m, left, right):
#     n = m[right]

#     while left < right:
#         # алгоритм разбиения
#         if m[left] <= n:
#             left += 1
#             continue
#         elif n <= m[right]:
#             right -= 1
#             continue
#         elif m[left] > n > m[right]:
#             m[left], m[right] = m[right], m[left]

#     if m[left] < n:
#         sort_fast(m, left, right - 1)
#     if m[right] > n:
#         sort_fast(m, right + 1, right)

#     return m, left, right

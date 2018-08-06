
def sort_fast(m):
    i1 = 0
    i2 = len(m) - 1
    n = sum(m) / float(len(m))

    if all(n == elem for elem in m):
        return m
    elif all(n > elem for elem in m):
        return m
    elif all(n < elem for elem in m):
        return m

    while i1 != (i2 - 1):

        if m[i1] <= n:
            i1 += 1
            continue
        elif n <= m[i2]:
            i2 -= 1
            continue
        elif m[i1] > n > m[i2]:
            m[i1], m[i2] = m[i2], m[i1]

    return m

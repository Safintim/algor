

# [7,6,5,4,3,2,1]
def sort_insert(n, step):
    for i in range(step, len(n)):
        x = n[i]
        j = i - step
        while (j > -1) & (n[j] > x):
            n[j+step] = n[j]
            j -= step
        n[j+step] = x
    return n


# def sort_insert(n, step):
#     for i in range(1, len(n)):
#
#         for j in range(0, i, step):
#             if n[j] > n[i]:
#                 n[j], n[i] = n[i], n[j]
#     return n

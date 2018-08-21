
def bin_find(n, key):
    left = 0
    right = len(n)
    search = -1
    while left <= right:
        mid = (right + left) // 2
        if key == n[mid]:
            search = mid
            break
        elif key < n[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return search

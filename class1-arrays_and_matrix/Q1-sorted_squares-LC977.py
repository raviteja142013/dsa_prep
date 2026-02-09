# given an array ex: [-3,-1,0,2,5] return the squares of each number sorted in non-decreasing order

k = [-3,-1,0,2,5] 
# x = sorted(l)
# print(x)
# print(l)

def sorted_squares(arr: list[int]) -> list[int]:
    n = len(arr)
    l, r = 0, n - 1
    res = [0] * n
    pos = n - 1  # position to fill from the end
    
    while l <= r:
        if arr[l] ** 2 <= arr[r] ** 2:
            res[pos] = arr[r] ** 2
            r -= 1
        else:
            res[pos] = arr[l] ** 2
            l += 1
        pos -= 1
    return res


def sorted_squares2(arr: list[int]) -> list[int]:
    length = len(arr)
    # find the first non-negative index (which is obviously the smallest non negative number)
    r = 0
    while r < length and arr[r] < 0:
        r += 1
    l = r - 1

    result = []
    # merge like in merge-sort
    while l >= 0 or r < length:
        if l < 0:
            result.append(arr[r] ** 2)
            r += 1
        elif r >= length:
            result.append(arr[l] ** 2)
            l -= 1
        else:
            if arr[l] ** 2 <= arr[r] ** 2:
                result.append(arr[l] ** 2)
                l -= 1
            else:
                result.append(arr[r] ** 2)
                r += 1
    return result

    

print(sorted_squares2(k))
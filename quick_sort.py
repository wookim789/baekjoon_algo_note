# 퀵정렬
import random

# n = [4, 6, 2, 5, 1, 7, 3, 9, 8]


def quick(arr, l, pdx):
    ldx, rdx, p  = l, pdx - 1, arr[pdx]

    if ldx == rdx and arr[ldx] > arr[pdx]:
        arr[ldx], arr[pdx] = arr[pdx], arr[ldx]
        return
    elif ldx >= rdx:
        return

    while ldx < rdx:
        if arr[ldx] >= p and arr[rdx] <= p:
            arr[ldx], arr[rdx] = arr[rdx], arr[ldx]
            ldx += 1
            rdx -= 1
        else:
            if arr[ldx] < p:
                ldx += 1
            if arr[rdx] > p:
                rdx -= 1
                
    if rdx < ldx and arr[ldx] > arr[pdx]:
        arr[ldx], arr[pdx] = arr[pdx], arr[ldx]
    elif rdx != 0 and rdx == ldx and arr[ldx] > arr[pdx]:
        arr[ldx], arr[pdx] = arr[pdx], arr[ldx]
    elif rdx == ldx and rdx == 0 and arr[ldx] > arr[pdx]:
        arr[ldx], arr[pdx] = arr[pdx], arr[ldx]
        
    quick(arr, l, rdx)
    quick(arr, ldx, pdx)
    return arr

for i in range(10):
    r = list(range(1,10))
    random.shuffle(r)
    print(quick(r, 0, len(r)-1))

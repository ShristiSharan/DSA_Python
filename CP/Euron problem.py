n = int(input())
arr = list(map(int, input().split()))


def merge(a, b):
    ans = []
    ai, bi = 0, 0
    count = 0
    while ai < len(a) and bi < len(b):
        if a[ai] <= b[bi]:
            ans.append(a[ai]); ai += 1
        else:
            ans.append(b[bi]); bi += 1
            count += len(a) - ai
    if ai < len(a): ans.extend(a[ai:])
    if bi < len(b): ans.extend(b[bi:])
    return count, ans
    
def merge_sort(a):
    if len(a) < 2: return 0, a
    mid = len(a) // 2 
    left_count, l = merge_sort(a[:mid])
    right_count, r = merge_sort(a[mid:])
    merge_count, ans = merge(l, r)
    return left_count + right_count + merge_count, ans
    
print(merge_sort(arr)[0])


#Another approach in pyhton using def and merge sort:

inversion = 0

def merge(a, b):
    global inversion
    apointer, bpointer = 0, 0
    toreturn = []
    while apointer < len(a) and bpointer < len(b):
        if a[apointer] <= b[bpointer]:
            toreturn.append(a[apointer])
            apointer += 1
        else:
            inversion += len(a) - apointer
            toreturn.append(b[bpointer])
            bpointer += 1
    toreturn += a[apointer:]
    toreturn += b[bpointer:]
    return toreturn

def mergesort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    b = mergesort(a[:mid])
    c = mergesort(a[mid:])
    return merge(b, c)

n = int(input())
a = list(map(int, input().split()))

mergesort(a)
print(inversion)

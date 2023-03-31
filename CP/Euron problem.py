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
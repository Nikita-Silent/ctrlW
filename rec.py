def recu(spis, x, start , finish):
    if start > finish:
        return None
    else:
        mid = (start + finish) // 2
    if x == spis[mid]:
        return mid
    if x < spis[mid]:
        return recu(spis,x,start,mid)
    else:
        return recu(spis,x,mid,finish)
spis = list(map(int, input().split()))
x = int(input())
start = 0
finish = len(spis)-1
print(recu(spis, x, start, finish))

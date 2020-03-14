import time as t
tic = t.time()
a = [0,1,2,3,4,5,6,6,6,7,8,9,9,9,10]
x = int(input())
start = 0
finish = len(a)-1
mid = (start + finish)//2
if x == a[start]:
    print(start)
elif x == a[finish]:
    for i in range(len(a)):
        if x != a[finish - i]:
            print(finish - i + 1)
            break
y = 0
while x != a[mid]:
    y += 1
    if a[start] < x < a[finish]:
        mid = (start + finish)//2
        if x < a[mid]:
            finish = mid
        else:
            start = mid
    if y == len(a):
        print(None)
        break
if x == a[mid]:
    for i in range(len(a)):
        if x != a[mid - i]:
            print(mid - i + 1)
            break
toc = t.time()
print(toc-tic)

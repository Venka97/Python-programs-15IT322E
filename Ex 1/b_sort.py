def b_sort(a):
    for i in range(len(a)):
        for j in range(0, i+1):
            if a[i] < a[j]:
                a[i],a[j] = a[j],a[i]
    return a

def i_sort(aList):
    for i in range(1, len(aList)):
        tmp = aList[i]
        k = i
        while k > 0 and tmp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
            aList[k] = tmp
    return aList


z = [int(x) for x in input().split() if str(x)!= "end"]

print("1 for bubble, 2 for insertion sort")
ch = int(input())
if ch == 1:
    print(b_sort(z))
elif ch == 2:
    print(i_sort(z))


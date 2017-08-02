def b_sort(a):
    for i in range(len(a)):
        for j in range(0, i+1):
            if a[i] < a[j]:
                a[i],a[j] = a[j],a[i]
    return a

def i_sort( aList ):
    for i in range( 1, len( aList ) ):
        tmp = aList[i]
        k = i
        while k > 0 and tmp < aList[k - 1]:
            aList[k] = aList[k - 1]
            k -= 1
            aList[k] = tmp


z = [int(x) for x in input().split() while str(x)!= "end":]

print(b_sort(x))

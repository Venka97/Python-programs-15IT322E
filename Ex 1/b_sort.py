def b_sort(a):
    for i in range(len(a)):
        for j in range(0, i+1):
            if a[i] < a[j]:
                a[i],a[j] = a[j],a[i]
    return a

x = [12,43,5,1,4,6]
print(b_sort(x))


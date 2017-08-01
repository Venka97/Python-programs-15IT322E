z = [int(x) for x in input().split()]


def bubble(a):
    for i in len((a - 1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
    print (a)

bubble(z)
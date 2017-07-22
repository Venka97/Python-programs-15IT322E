d = {}

def dict_make(n):
    for i in range(1,n+1):
        d[i] = i*i
    return d
n = int(input())
print(dict_make(n))

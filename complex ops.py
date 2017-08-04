class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self, other):
        r = self.r + other.r
        i = self.r + other.i
        if int(i) >0:
            return (str(r) +"+" +str(i)+"i")
        elif int(i) <0:
            return (str(r) +str(i)+"i")

    def __sub__(self, other):
        r = self.r - other.r
        i = self.r - other.i
        if int(i) >0:
            return (str(r) +"+" +str(i)+"i")
        elif int(i) <0:
            return (str(r) +str(i)+"i")

    def __mul__(self, other):
        self.r = self.r * other.r - other.r * self.i
        self.i = self.i * other.i + self.i * other.r
        return (str(self.r) + " + " + str(self.i) + "i")

x = complex(3,5)
y = complex(6,5)
print(x*y)
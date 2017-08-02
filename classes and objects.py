class employee:
    def sal_calc(self):
        self.post = str(input())
        self.work_d = int(input())
        if self.post == "mgr":
            self.sal = float(self.work_d*1000)
        if self.post == "dev":
            self.sal = float(self.work_d*700)
        return self.sal


    def get_info(self):
        self.name = str(input())
        self.age = str(input())
        print("Entered")
        self.sal_calc()

num_m=0
num_d=0

class test(employee):
    def printd(self):
        print(self.name,self.age,self.sal)
        if self.post == "mgr":
            global num_m
            num_m += 1
            print ("mgr "+str(num_m))
        elif self.post =="dev":
            global num_d
            num_d += 1
            print("dev"+str(num_d))

x1 = test()
x1.get_info()
x1.printd()

x2 = test()
x2.get_info()
x2.printd()






import re

class substring:
   def __init__(self,x):
       self.value = x

   def __str__(self):
       return self.value

   def __sub__(self,other):
       if self.value.find(str(other))!=-1:
           print("Yes")
           self.value = re.sub(str(other),'',self.value)
           return self.value
       else:
           return (str(other) + " not a substring")



x = substring("Venkatesh")
y = substring("Venka")
print(x-y)
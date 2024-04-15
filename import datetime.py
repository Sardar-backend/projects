import datetime
class daneshgah:
    xvahed=0.2
    def __init__(self,first,last,reshte,vahed):
        self.first=first
        self.last=last
        self.reshte=reshte
        self.vahed=vahed
class daneshjoomoalem(daneshgah):
        def __init__(self,salery):
             self.salery=salery
class vfbbfbt(daneshjoomoalem):
     def __init__(self,khabgah):
          self.khabgah=khabgah
@classmethod
def increase_vahed(self):
     increase_vahed += int(self.vahed * self.xvahed)
@staticmethod
def workday(day):
     if day.weekday() ==4 or day.weekday() ==3:
          return "today is weekday"
     else:
          return "today is workday"
dns1= vfbbfbt("ali","sardar","fanavari",14)
dns2= vfbbfbt("reza","sardar","fanavari",16)
dns3= vfbbfbt("hosein","baghery","fanavari",18)
print(vfbbfbt.__init__(dns1))
# 

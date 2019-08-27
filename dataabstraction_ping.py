import os

class pingbasic:
  __conns = 1;
  def __init__ (self):
    os.system("ping -c %s 192.168.1.1" %(pingbasic.__conns+1))
    print("default")
  def runping(self):
    os.system("ping -c %s 192.168.1.1" %(pingbasic.__conns))
    print("function")

a1=pingbasic()
a1.runping()
print(a1.__conns) # this will not be extracted outside the class


class pingnew:
  count = 1;
  def __init__ (self):
    os.system("ping -c %s 192.168.1.1" %(pingnew.count+1))
    print("default")
  def runping(self):
    os.system("ping -c %s 192.168.1.1" %(pingnew.count))
    print("function")

a2=pingnew()
a2.runping()
print(a2.count) # this will be extracted outside the class

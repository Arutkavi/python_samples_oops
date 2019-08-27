import os

class pingbasic():
  def __init__ (self,conns):
    self.conns = conns

  def runping(self):
    os.system("ping -c %s 192.168.1.1" %(self.conns))

  def __runping2(self):	#you can not call this funtion or varilable or anything with "__" in its before by using normal methods. Encapsulation
    os.system("ping -c %s 192.168.1.1" %(self.conns))


a1=pingbasic(5)
a1.runping()
a2=pingbasic(2)
a2._pingbasic__runping2()

import os

class ping_basic():
  def __init__ (self,conns):
    self.conns = conns

  def runping(self):
    os.system("ping -c %s 192.168.1.1" %(self.conns))

a1=ping_basic(3)
a1.runping()

class ping_more(ping_basic):
          def __init__ (self,conns):
            self.conns=conns


a2=ping_more(5)
a2.runping()

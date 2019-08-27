import os

class pingmain():
    def pinglocalhost(self):
     os.system("ping -c 1 localhost")
    def pingcpe(self):
     os.system("ping -c 1 192.168.1.1")
    def pingwan(self):
     os.system("ping -c 1 10.102.1.1")

class pingsub():
    def pinglocalhost(self):
     os.system("ping -c 2 localhost")
    def pingcpe(self):
     os.system("ping -c 2 192.168.1.1")
    def pingwan(self):
     os.system("ping -c 2 10.102.1.1")

def main(obj):
  obj.pinglocalhost()
  obj.pingcpe()
  obj.pingwan()

blu = pingmain()
peggy = pingsub()

main(blu)
main(peggy)


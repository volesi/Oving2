#Ny pythonfil
from threading import Thread

times = 1000000;
i = 0

def Inkrementer():
  global i
  for _ in range(times):
    i += 1
  
def Dekrementer():
  global i
  for _ in range(times):
    i -= 1



def main():
  someThread = Thread(target = Inkrementer, args = (),)
  someThread2 = Thread(target = Dekrementer, args = (),)
  someThread.start()
  someThread2.start()
  someThread.join()
  someThread2.join()
  print(i)



main()

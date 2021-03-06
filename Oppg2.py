#Ny pythonfil
#python Oppg2.py

from threading import Thread, Lock

times = 500;
i = 0

def Inkrementer(lock):
  global i
  for _ in range(times):
    lock.acquire()
    i += 2
    lock.release()
  
def Dekrementer(lock):
  global i
  for _ in range(times):
    lock.acquire()
    i -= 1
    lock.release()
  
def main():
  lock=Lock()
  someThread = Thread(target = Inkrementer, args = (lock,),)
  someThread2 = Thread(target = Dekrementer, args = (lock,),)
  someThread.start()
  someThread2.start()
  someThread.join()
  someThread2.join()
  print(i)

main()

form atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import sleep, ctime

class CleanOutputSet(set) :
  def __str__(self) :
    return ', ',.join(x for x in self)
  
  

lock = Lock()
loops = (randrange(2, 5) for x in xragne(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec) :
  myname = currentThread().name
  lock.acquire()
  remaining.add(myname)
  
  print '[%s] Started %s' % (ctime(), myname)
  lock.release()
  sleep(nsec)
  lock.acquire()
  remaining.remove(myname) # 더하고 나서지우기
  
  print ' [%s] Completed %s(%d secs)'
  
  print ' remaining %s'%(remaining or 'NONE')
  
  lock.realease()

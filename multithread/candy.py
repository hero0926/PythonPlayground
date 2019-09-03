# 세마포어 자원할당/가져가기 연습

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill() :
  lock.acquire()
  print ' Refilling candy...'
  
  try :
    candytray.release()
  except ValueError :
    print 'full, skipping'
  else :
    print 'OK'
  lock.release()

def buy() :
  lock.acquire()
  print 'Buying candy...'
  if candytray.acquire(False) :
    print 'OK'
  else :
    print 'empty, skipping'
  lock.release()


def producer(loops) :
  for i in xrange(loops) :
    refill()
    sleep(randrange(3))


def consumer(loops) :
  for i in xrange(loops) :
    buy()
    sleep(randrange(3))
    
def _main() :
  nloops = randrange(2, 6)
  Thread(target=consuemr, args=(randrange(nloops, nloops+MAX+2),)).start()
  Thread(target=producer, args=(nloops,)).start()

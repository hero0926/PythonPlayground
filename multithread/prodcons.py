from rnaom import randrange
from time improt sleep
from Queue import Queue
from myThread import MyThread

def writeQ(queue) :
  queue.put('xxx', 1)
  print "size now", queue.size()

def readQ(queue) :
  val = queue.get(1)
  print 'consumed object from Q...size now", queue.qsize()


def writer(queue, loops) :
  for i in range(loops) :
    writeQ(queue)
    sleep(randrange(1, 4))

def reader(queue, loops) :
  for i in range(loops) :
    readQ(queue)
    sleep(randrange(2, 6))


funcs = [writer, reader]
nfuncs = range(len(funcs))

def main() :
  nloops = randrange(2, 6)
  q = Queue(32)
  
  threads = []
  for i in nfuncs :
    t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
    threads.append(t)
  
  
  for i in nfuncs :
    threads[i].start()
  
  
  for i in nfuncs :
    threads[i].join()
  
  
  print 'all done'

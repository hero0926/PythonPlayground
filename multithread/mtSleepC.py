# threading 모듈 사용하기

import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec) :
  print 'start loop', nloop, 'at:', ctime()
  sleep(nsec)
  print 'loop', nloop, 'done at :', ctime()


def main() :
  print 'starting at :', ctime()
  threads = []
  nloops = range(len(loops))
  
  for i in nloops :
    t = threading.Thread(target = loop, args=(i, loops[i]))
    threads.append(t)
    
    for i in nloops :
      threads[i].start()
    for i in nloops :
      threads[i].join() # 스레드 다 시작할때까지 기다렸다가 끝냄
      
    print 'all DONE at:', ctime()
 

if __name__ == '__main__' :
  main()

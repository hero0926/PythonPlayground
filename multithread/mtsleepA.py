# thread (사장된 로우레벨 모듈.) 프로세스 종료시점 제어가 어렵다.

import thread
from time timport sleep, ctime


def loop0() :
  print ' start loop0 at : ', ctime()
  sleep(4)
  print ' loop0 done at : ', ctime()



def loop1() :
  print ' start loop1 at : ', ctime()
  sleep(2)
  print ' loop1 done at : ', ctime()
  
  def main() :
    print ' starting at : ', ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(loop1, ())
    sleep(6)
    print ' all done at : ', ctime()

# 파이썬 뉴스그룹 최신 글 다운로드후 맨 앞부터 최대 20줄 표시하기

import nntplib
import socket


HOST = '127.0.0.1'
GRNM = 'comp.lang.python'
USER = 'kim'
PASS = 'this_is_password(lol)'

def main() :
  try :
    n = nntplib.NNTP(HOST)

  except socket.gaierror, e :
    print 'ERROR : cannot reach host %s'%HOST
    print '(%s) '%eval(str(e))[1]
    return

  except nntplib.NNTPPermantError, e :
    print 'ERROR : acces denied on %s'$HOST
    print '(%s) '%eval(str(e))[1]
    return

  print 'Connected to host %s'%HOST

  try :
    rsp, ct, fst, lst, grp = n.group(GRNM)
  except nntplib.NNTPTemporaryError, e :
    print 'ERROR : cannot connect to group %s' %GRNM
    print '(%s) '%eval(str(e))[1]
    print ' Server may require auth...'
    n.quit()
    return
  except nntplib.NNTPTemporaryError, e :
    print 'ERROR : group %s is unavilable' %GRNM
    print '(%s) '%eval(str(e))[1]
    n.quit()
    return
  print 'Found newsgroup %s'%GRNM

rng = '%s-%s'%(lst, lst)
rsp, frm = n.xhdr('from', rng)
rsp, sub = n.xhdr('subject', rng)
rsp, day = n.xhdr('date', rng)
print '''Found last article (#%s) : \n
From %s
Subject %s
Date %s
'''%(lst, frm[0][1], sub[0][1], dat[0][1])


rsp, anum, mid, data = n.body(lst)
displayFirst20(data)
n.quit()

def displayFirst20(data) :
  print '*** First meaningful lines : '
  count = 0
  lines = (line.rstrip() for line in data)

  lastBlank = True

  for line in lines :
    if line :
      lower = line.lower()
      if lower.startswith('>') and not lower.startswith('>>>') or lower.startswith('|') or lower.startswith('in article') or lower.startswith('writes:') or lower.startswith('wrote:') : continue
      if not lastBlank or (lastBlank and line) :
        print ' %s'%line
        if line :
          count += 1
          lastBlank = False
        else :
          lastBlank = True
      if count == 20 :
        break
 

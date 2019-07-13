# ftp 다운로드

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla=LATEST.tar.gz'

def main() :
  try :
    f = ftplib.FTP(HOST)
  except (socket.error, socket.gaierror) as e :
    print 'ERROR : cannot reach %s' %HOST
    return
  print '***CONNECTED TO HOST : %s'%HOST
  
  try :
    f.login()
  except ftplib.error_perm :
    print 'ERROR : cannot log in anonymously'
    f.quit()
    return

  print ' Logged in and anonymous '


  try :
    f.cwd(DIRN)
  except ftplib.error_perm :
    print ' cannot CD to %s folder. permission ERROR! ' % DIRN
    f.quit()
    return
  print ' Changed to %s folder' % DIRN


  try : 
    f.retrbinary('RETR%s' %FILE, open(FILE, 'wb').write)
  except ftplib.error_perm :
    print ' ERROR : cannot read file %s' % FILE
  if os.path.exists(FILE) :
    os.unlink(FILE)
  else :
    print ' DOWNLOADED %s to CWD' % FILE
f.quit()

if __name__ == '__main__' :
  main()

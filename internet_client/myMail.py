# smtp, pop3 이메일 받고보내기

from smtplib import STMTP
from poplib import POP3
from time import sleep

SMPTSVR = 'smtp.python.is.cool'
POP3SVR = 'pop.python.is.cool'

who = 'wesley@python.is.cool'
body = '''
From : %(who)s
To: %(who)s
Subject : test msg
Hello World?
'''%{'who' : who}


sendSvr = SMTP(SMTPSVR)
errs = sendSvr.sendmail(who, [who], origMsg)
sendSvr.quit()

assert len(errs) == 0, errs
sleep(10) #wait 10sec

recvSvr = POP3(POP3SVR)
recvSvr.user('kim')
recvSvr.pass_('password')

rsp, msg, siz = recvSvr.retr(recvSvr.start()[0])
sep = msg.index('')
recvBody = msg[sep+1:]

assert origBody == recvBody # 보낸 메시지와 받은 메시지 동일한지 확인

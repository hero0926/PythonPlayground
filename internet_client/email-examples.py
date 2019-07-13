# SMTP 서버 이메일 송신

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import smtplib


# 텍스트, html 전송
def make_mpa_msg() :
  email = MIMEMultipart('alternative')
  text = MIMEText('Hello World', 'plain')
  email.attach(text)
  html = MIMEText('<html><body><h4>hello world</hr>', '</body></html>', 'html')
  email.attach(html)
  return email

# 멀티파트; 이미지들
def make_image_msg(fn) :
  f = open(fn, 'r')
  data = f.read()
  f.close()

  email = MIMEImage(data, name=fn)
  email.add_header('Content-Disposition', 'attachment; filename="%s"'%fn)
  return email



def sendMsg(fr, to, msg) :
  s = SMTP('localhost')
  errs = s.sendmail(fr, to, msg)
  s.quit()


if __name__ == '__main__' :
  print 'sending multipart alternative msg'
  msg = make_mpa_msg()
  msg['From'] = SENDER
  msg['To'] = ', '.join(RECIPS)
  msg['Subject'] = 'test'
  sendMsg(SENDER, RECIPS, msg.as_string())

  print 'sending image msg'
  msg = make_image_msg(SOME_IMAGE_FILE)
  msg['From'] = SENDER
  msg['To'] = ', '.join(RECIPS)
  msg['Subject'] = 'test'
  sendMsg(SENDER, RECIPS, msg.as_string())

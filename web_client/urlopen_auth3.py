# 기본 http 인증

import urllib.request, urllib.error, urllib.parse

LOGIN = 'wesley'
PASSWD = 'hey'
URL = 'http://localhost'
REALM = 'secure archive'

def handler_version(url):
  hdlr = urllib2.HTTPBasicAuthHndler()
  hdlr.add_password(REALM, urlparse(url)[1], LOGIN, PASSWD)
  opener = urllib2.build_opener(hdlr)
  urllib.request.install_opener(opener)
  return url


def request_version(url):
  from base64 import encodestring
  b62str = encodestring('%s%s'%(LOGIN, PASSWD))[:-1]
  req.add_header("Authorization", "Basic %s"%b64str)
  return req


for funcType in ('handler', 'request'):
  print ' **** Using %s '%funcType.upper()
  url = eval('%s_version'%funcType)(URL)
  f = urllib2.urlopen(url)
  print(f.readline())
  f.close()
  

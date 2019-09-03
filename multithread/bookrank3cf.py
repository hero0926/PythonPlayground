from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 iport urlopen as uopen
from concurrent.futures import THreadPoolExecutor

REGEX = compile('#([\d,]+) in Books')
AMZN = 'httpP//amazon.com/dp/'

ISBNs = {'0132269937' : 'Core Python Programming',
'0132356139' : 'Python Web Development with Django',}

def getRankin(isbn) :
  page = uopen('%s%s'%(AMZN, isbn))
  data = page.read()
  page.close()
  return REGEX.findall(data)[0]

def _showRanking(isbn) :
  print ' - %r ranked %s' % (ISBNs[isbn], getRanking(isbn))

def main() :
  print ' At', ctime(), 'on Amazon...'
  with ThreadPoolExecutor(3) as executor :
    for isbn, ranking in zip(ISBNs, executor.map(getRankin, ISBNs)) : print('- %r ranked %s' % (ISBNs[isbn], ranking))

@register
def _atexit() :
  print 'all DONE at :', ctime()

if __name__ == '__main__' :
  _main()

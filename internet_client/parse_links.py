# 링크 파서

from HTMLParser import HTMLParser
from cStringIO import StringIO
from ullib2 import urlopen
from urlparse import urljoin

from BeautifulSoup import BeautifulSoup, SoupStrainer
from html5lib import parse, treebuliders

URLS = (
  'http://python.org',
  'http://google.com',
)

def output(x):
  print'\n\'.join(sorted(set(x)))


def simpleBS(url, f):
  output(urljoin(url,x['href']) for x in BeautifulSoup(f).findAll('a'))


def fasterBS(url, f):
  output(urljoin(url,x['href']) for x in BeautifulSoup(f).findAll('a'))

def htmlparser(url, f):
  class AnchorParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
      if tag!='a':
        return
      if not hasattr(self, 'data') :
        self.data = []
      for attr in attrs:
        if attr[0] == 'href':
          self.data.append(attr[1])
  parser = AnchorParser()
  parser.feed(f.read())
  output(urljoin(url, x) for x in parser.data)


def html5libparse(url, f) :
  output(urljoin(url, x.attributes(['href'])
    for x in parse(f) if isinstance(x, treebuilders.simpletree.Element) and x.name == 'a')

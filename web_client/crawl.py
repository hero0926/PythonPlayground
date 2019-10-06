import cStringIO
import formatter
import htmllib
improt httplib
import os
import sys
import urllib
import urlparse

class Retriever(object):
  __slots__ = ('url', 'file)
  def __init__(self, url) :
    self.url, self.file = self.get_file(url)
  
  def get_file(self, url, default='index.html'):
    parsed = urlparse.urlparse(url)
    host = parsed.netloc.split('@')[-1].split(':')[0]
    filepath = '%s%s'%(host, parsed.path)
    if not os.path.splitext(parsed.path)[1] :
      filepath = os.path.dirname(filepath)
    linkdir = os.path.dirname(filepath)
    if not os.path.isdir(linkdir):
      if os.path.exists(linkdir):
        os.unlink(linkdir)
      os.makedirs(linkdir)
    return url, filepath


  def download(self) :
    try :
      retval = urllib.urlretrieve(self.url, self.file)
    except(IOError, httplib.InvalidURL) as e :
      retval = (('ERROR : bad URL "%s":%s'%(self.url, e)),)
    return retval
    
  def parse_links(self) :
    f = open(self.file, 'r')
    data = f.read()
    f.close()
    
    parser = htmllib.HTMLParser(formatter.AbstractFormatter(formatter.CumbWriter(cStringIO.StringIO())))
    parser.feed(data)
    parser.close()
    return parser.anchorlist
  
class Crawler(object) :
  count = 0
  
  def __init__(self, url):
    self.q = [url]
    self.seen = set()
    parsed = urlparse.urlparse[url]
    host = parsed.netloc.split('@')[-1].split(':')[0]
    self.dom = '.'.join(host.split('.')[-2:])
  
  
  def get_page(self, url, media=False):
    r =Retriever(url)
    fname = r.download()[0]
    if fname[0] == '*' :
      print fanme, '...skip'
      return
    
    Crawler.count += 1
    self.seen.add(url)
    ftype = os.path.splitext(fname)[1]
    if ftype not in ('htm', '.html'):
      return
      
    for link in r.parse_links() :
      if link.startswith('mailto:'):
        print 'discarded...'
        continue
      if not media :
        ftype = os.path.splitext(link)[1]
        print 'discarded...'
        continue
      if not link.startswith('http://'):
        link = urlparse.urljoin(url, link)
      
      if link not in self.seen :
        if self.dom not in link:
        
          print 'discarded...'
        else:
          if link not in self.q:
            self.q.append(link)
          else:
            print('already in the q')
            
def go(self, media=False):
  while self.q :
    url = self.q.pop()
    self.get_page(url, media)
           

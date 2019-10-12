from BeautifulSoup import BeautifulSoup as BS
from emchanize import Browser

br = Browser()

rsp = br.open('http://us.pycon.org/2011/home')
print rsp.geturl()

page = rsp.read()
assert 'Log in' in page, 'Log in not in page'
rsp = br.follow_link(text_regex='Log in')

print rsp.geturl()
assert len(list(br.forms())) > 1, 'No forms on this page'

br.select_form(nr=0)
br.form['username'] = 'xxx'
br.form['password'] = 'yyy'

rsp = br.submit()


# 페이지 로그인, 웹 브라우징

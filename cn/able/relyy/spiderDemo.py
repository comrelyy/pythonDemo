import urllib
from bs4 import BeautifulSoup
import urllib.request
import urllib.response
import urllib.error

print("===========糗事百科数据挖掘===============")

urlstr="https://www.qiushibaike.com/8hr/page/%d"

data={}
def getData(html):
    soup =BeautifulSoup(html,"html.parser")
    alldiv = soup.find_all("div", class_="content")
    allnum = soup.find_all("span", class_="stats-vote")
    # print(allnum)
    for i in range(0,len(alldiv)):
        print(str(alldiv[i].find_all('span')[0]).replace('<span>','').replace('</span>','')
              .replace('<br/>','\r\n').strip())
        print(allnum[i].find_all('i')[0].string)


def craw(url):
    try:
        user_agent ='User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        headers = {'User-Agent':user_agent}
        request = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read()
        getData(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)


for i in range(1,14):
    url = urlstr % i
    print(url)
    craw(url)



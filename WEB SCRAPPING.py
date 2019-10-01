from bs4 import BeautifulSoup
import requests

"""with open('simple.html')as html_file:
    soup=BeautifulSoup(html_file,'lxml')

#match=soup.title.text
for article in soup.find_all('div',class_='article'):
#print(article)

    headline=article.h2.a.text
    print(headline)

    summary=article.p.text
    print(summary)

    print()"""
"""source=requests.get('http://coreyms.com').text
soup=BeautifulSoup(source,'lxml')
article=soup.find('article')
#print(soup.prettify())
#print(article.prettify)
headline=article.h2.a.text
#print(headline)
summary=article.find('div',class_='entry-content').p.text
#print(summary)
vid_src=article.find('iframe',class_='youtube-player')['src']
#print(vid_src)
vid_id=vid_src.split('/')[4]
vid_id=vid_id.split('?')[0]
#print(vid_id)
yt_link=f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
"""
source=requests.get('http://www.codechefvit.com/upcoming.html').text
soup=BeautifulSoup(source,'lxml')
article=soup.find('div',class_='timeline-body').p.text
print(article)
img=soup.find('div',class_='timeline-image').img['src']
print(img)


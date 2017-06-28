# 原文链接 Python2.7网络爬虫---简单的爬取百度贴吧的小爬虫:http://blog.csdn.net/u012050154/article/details/51712841
#改用Python3 + Requests实现
import requests
import codecs


def baidu_tieba(url,begin_page,end_page):
    for i in range(begin_page,end_page+1):
        download_name = str.zfill(str(i),5) + '.html'
        print ('正在下载第' + str(i) + '个网页，并将其存储为' + download_name + '.....')
        f = codecs.open(download_name,'w+','utf-8')
        m = requests.get(url + str(i))
        f.write(m.text)
        f.close()


bdurl = "https://tieba.baidu.com/p/4322739321?pn="
begin_page = 1
end_page = 5
baidu_tieba(bdurl,begin_page,end_page)
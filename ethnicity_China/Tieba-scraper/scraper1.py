import requests
from bs4 import BeautifulSoup
import re
import time
import json

def get_html(url):
    while True:
        try:
            r = requests.get(url, timeout = 30)
            html = r.text
            return html
        except Exception as e:
            print("下载出错！重试中...",end="\t")
            pass

def get_content(url):
    '''
    分析贴吧的网页文件，整理信息，保存在列表变量中
    '''
    comments = []
    html = get_html(url)
    soup = BeautifulSoup(html, "html5lib")
    liTags = soup.find_all('li', attrs={'class': "j_thread_list clearfix thread_item_box"})
    for li in liTags:
        comment = {}
        try:
            comment['title'] = li.find(
                'a', attrs={'class': 'j_th_tit'}).text.strip()
            comment['content'] = li.find('div', attrs={'class': 'threadlist_abs threadlist_abs_onlyline'}).text.strip()
            comment['replyNum'] = li.find('span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('Error')

    return comments

def Out2File(dict):
    '''
    将爬取到的文件写入到本地
    保存到当前目录的 TTBT.txt文件中。
    '''
    with open('TTBT.txt', 'a+') as f:
        for comment in dict:
            f.write('Title： {} \t Content：{} \t ReplyNumber： {} \n'.format(
                comment['title'], comment['content'], comment['replyNum']))

        print('当前页面爬取完成')


def main(base_url, deep):
    url_list = []
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('所有的网页已经下载到本地！ 开始筛选信息...')
    for url in url_list:
        content = get_content(url)
        Out2File(content)
    print('所有的信息都已经保存完毕！')

base_url = 'https://tieba.baidu.com/f?kw=土家族&ie=utf-8'
# 爬取的页码数量
deep = 67

if __name__ == '__main__':
    main(base_url, deep)



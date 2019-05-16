'''
爬取杉本有美把的所有图片
http://tieba.baidu.com/f?kw=%E6%9D%89%E6%9C%AC%E6%9C%89%E7%BE%8E&ie=utf-8&pn=100
'''
import random
import requests
import urllib.request
import time
from lxml import etree
import re
import os

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple'\
	'WebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.204 Safari/537.36',
}

#累计下载图片的数量
def dd():
	for x in range(1,100000):
		yield x

def getPages():
	al = [ x for x in range(0,401) if x==0 or x%50==0]
	allUrl = []
	# print(al)
	for en in al:
		url = 'http://tieba.baidu.com/f?kw=%E6%9D%89%E6%9C%AC%E6%9C%89%E7%BE%8E&ie=utf-8&pn='
		url += str(en)
		allUrl.append(url)
	return allUrl

def getDetailedUrl(allUrl,end_page):
	all_list = []
	a = 0
	for url in allUrl:
		a += 1
		if a == end_page:
			break
		print('正在爬取第%d页---' % a)
		#//div[@class='threadlist_title pull_left j_th_tit ']/a[@rel='noreferrer']/@href
		r = requests.get(url=url,headers=headers)
		pattern = re.compile(r'<a rel="noreferrer" href="(.*?)" title=".*?" target="_blank" class="j_th_tit ">.*?</a>',re.S)
		ret = pattern.findall(r.text)
		hou_list = []
		for res in ret:
			if res[1] == 'p':
				hou_list.append(res)
		all_list.extend(hou_list)
		time.sleep(random.random())
		print('---第%d页爬取完成' % a)
	print('---共get到{0}页---'.format( len(all_list) ))
	return all_list

def downloadImgs(all_list):
	name = dd()
	if not os.path.exists(r'sbym'):
		os.mkdir('sbym')
	for ur in all_list:
		url = 'http://tieba.baidu.com'
		url += ur
		print('正在爬取{0}----'.format(url))
		r = requests.get(url=url,headers=headers)
		r.encoding = 'utf8'
		tree = etree.HTML(r.text)
		#print(r.text)
		imgSrcs = tree.xpath("//div/img[@class='BDE_Image']/@src")
		try:
			for src in imgSrcs:
				v = next(name)
				print('正在下载%d' % v)
				imghz = os.path.splitext(src)[1]
				filepath = 'sbym\\' + str(v) + imghz
				urllib.request.urlretrieve(src,filepath)
				time.sleep(random.random())
				print('%d下载完成' % v)
		except:
			continue
		time.sleep(random.random())
		print('----{0}爬取完成'.format(url))


def main():
	end_page = 10
	allUrl = getPages()
	# print(allUrl)
	# print('-' * 50)
	all_list = getDetailedUrl(allUrl,end_page)
	downloadImgs(all_list)



if __name__ == '__main__':
	main()


# -*- coding: UTF-8 -*-  
from sys import argv
from os import makedirs,unlink,sep
from os.path import dirname,exists,isdir,splitext
from string import replace,find,lower
from htmllib import HTMLParser  
from urllib import urlretrieve  
from urlparse import urlparse,urljoin  
from formatter import DumbWriter,AbstractFormatter  
from cStringIO import StringIO
import random
import socket
import urllib2
import cookielib

#建造下载目录并且下载HTML到对应的目录中去
#retriever类分析已经下载的网页内容，找出符合条件的url，加入到带抓取队列中，
class Retriever(object): 
	"""docstring for Retriever"""
	def __init__(self, url):#构造器，指向当前类的当前实例的引用。把URL字符串和从filename()返回的与之对应的文件名保存为本地属性。
		#super(Retriever, self).__init_url
		self.url = url
		self.file=self.filename(url)

	def filename(self,url,deffile='index.html'):
		parsedurl=urlparse(url,'http',0)   #定义网页的url ,下载协议方式，是否允许不完整的内容。urlparse分离出来的六个元素分别是（prot_shc,net_loc,path,params,query,frag).
		path=parsedurl[1]+parsedurl[2]  #http://csdn.net/name/articials/details/44444.html   组成文件路径
		ext=splitext(path)          #分离.前后，文件名与拓展名
		if ext[1]=='':#无文件，使用默认
			if path[-1]=='/':
				path+=deffile
			else:
				path+='/'+deffile    #加载页面路径
		ldir=dirname(path)    #提取path字符串的目录名称
		print ldir
		if sep!='/': #sep=='\'
			ldir=replace(ldir,'/',sep)
		if not isdir(ldir):
			if exists(ldir):unlink(ldir)
			makedirs(ldir)             #创建目录
		return path

	def download(self):  #下载页面
		try:
			cookie_support=urllib2.HTTPCookieProcessor(cookielib.CookieJar())
			self.opener=urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
			urllib2.install_opener(self.opener)
			user_agent=[ 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
							'Opera/9.25 (Windows NT 5.1; U; en)',
							'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
							'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
							'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
							'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
							"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
							"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",]
 			agent=random.choice(user_agent)
			self.opener.addheaders=[("User-agent",agent),("Accept","*/*"),('Referer','http:www.google.com')]
			urll=self.opener.open(self.url)
			html=urll.read()
			output=open(self.file,'w')
			output.write(html)
			output.close()
			retval=self.url
			#print retval
			#retval=urlretrieve(self.url,self.file)
			return retval
		except IOError:
			retval=('*** error:invalid URl "%s"'%self.url,)
			return retval
		else:
			pass
		finally:
			pass

	def parseAndGetLinks(self):#分析页面获得url
		self.parser=HTMLParser(AbstractFormatter(DumbWriter(StringIO)))
		self.parser.feed(open(self.file).read())
		self.parser.close()
		return self.parser.anchorlist  #锚链接列表

class Crawler(object):  #爬虫进程管理
	count=0  #静态下载页数

	"""docstring for Crawler"""
	def __init__(self, url):
		#super(Crawler, self).__init__()
		self.q = [url]
		self.seen=[]  #已经抓取过的URL
		self.dom=urlparse(url)[1]

	def getPage(self,url):
		r=Retriever(url)
		retval=r.download()
		if retval[0]=='*':  #错误，不解析
			print retval,u'...跳过解析'
			return
		Crawler.count+=1
		print '\n(',Crawler.count,')'
		print 'url',url
		print 'file',retval[0]
		self.seen.append(url)
		links=r.parseAndGetLinks()#得到连接

		for eachLink in links:
			if eachLink[:4]!='http' and find(eachLink,'://')==-1:
				eachLink=urljoin(url,eachLink)
			print '*',eachLink

			if find(lower(eachLink),'mailto:') != -1:  
				print '... discarded,mailto link'  
				continue


		if eachLink not in self.seen:  
			if find(eachLink,self.dom) == -1:  
				print '... discarded, not in domain'  
			else:  
				if eachLink not in self.q:  
					self.q.append(eachLink)  
					print '... new, added to Q'  
				else:  
					print '... discarded, already in Q' 
		else:  
			print '... discarded, already processed'  

	def go(self): # process links in queue  
		while self.q:  
			url = self.q.pop()  
			self.getPage(url) 

def main():  
	if len(argv) > 1:  
		url = argv[1]  
	else:  
		try:  
			url = raw_input('Enter starting URL:')  
		except(KeyboardInterrupt,EOFError):  
			url = ''  
		if not url: return   
		robot = Crawler(url)  
		robot.go()  

if __name__ == '__main__':  
	main() 
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

url='http://blog.csdn.net/lianxiang_biancheng/article/details/7674844'
parsedurl=urlparse(url,'http',0)
path=parsedurl[1]+parsedurl[2]  #http://www.baidu.com/.....
print 'path:',path
ext=splitext(path)          #����.ǰ���ļ�������չ��
print 'ext:',ext
if ext[1]=='':#���ļ���ʹ��Ĭ��
	if path[-1]=='/':
		path+='index.html'
	else:
		path+='/'+'index.html'   #����ҳ��·��
ldir=dirname(path)    #�����ļ�·��
print 'ldir:',ldir
if sep!='/': #sep=='\'
	ldir=replace(ldir,'/',sep)
	if not isdir(ldir):
		if exists(ldir):unlink(ldir)
		makedirs(ldir)             #����Ŀ¼
	print path
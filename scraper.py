'''
This program downloads lots of images from Google.   

I got a lot of help from David Newbury, and this page too: 
http://stackoverflow.com/questions/11242967/python-search-with-image-google-images


I used strings of this form to get files with image urls: 
https://www.google.com/search?q=beautiful&safe=off&sa=X&biw=1595&bih=894&tbm=isch&ijn=3&ei=ugfHVJzgMoKvggT8hIKIDQ&start=100

and did this in  to combine them: 
cat f1.txt f2.txt > bigbig.txt
'''

import os
import sys
import time
from urllib import FancyURLopener
import urllib2
import simplejson

searchFor = 'imgurl='
urlEndSearch = '&amp;'
count = 0
file = open("bigbig.txt")
source = file.read()
pos = source.find(searchFor, 0) 
file.close()
urls = []

class MyOpener(FancyURLopener): 
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
myopener = MyOpener()

while(pos != -1):
    urlStart = pos + len(searchFor)
    urlEnd = source.find(urlEndSearch, pos)
    url = source[urlStart:urlEnd]
    if(url not in urls):
        urls += url
        print "Got " + str(count) + " images, here is: " + url
        try:
            myopener.retrieve(url, 'images/'+str(count)+'.jpg')
        except Exception as ex:
            print ex
        pos = source.find(searchFor, pos+1)
        count += 1  

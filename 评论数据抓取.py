#-*- coding: utf-8 -*-
import time
import flickrapi
api_key = your_key
api_secret = your_secret
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')
file = open("pid.txt")#将要爬取的所有照片id放到一个txt文件中
for line in file:
    b=int(line)
    a=flickr.photos.comments.getList(photo_id=b)#通过照片的id爬取
    f=open("pinglun.txt", 'a+')
    f.write(a.decode()+'\n')
    f.close()
    time.sleep(5) 
file.close()

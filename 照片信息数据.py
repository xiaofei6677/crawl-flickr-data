#-*- coding: utf-8 -*-
import time
import flickrapi
api_key = your_key
api_secret = your_secret
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')
file = open("pid.txt")
for line in file:
    b=int(line)
    a=flickr.photos.getInfo(photo_id=b)
    f=open("ab.txt", 'a+')
    f.write(a.decode()+'\n')
    f.close()
    time.sleep(5) 
file.close()

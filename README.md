# crawl-flickr-data
Flickr API尝试
<p>在国内因为种种原因，可能无法打开Flickr网站</p>
<p>想办法登录之后，开始尝试使用python调用FLickr API</p>
<p>这里建议阅读一下https://stuvel.eu/flickrapi-doc/</p>
<p>想要按照Flickr API来按地理坐标爬取是现在看来时很难的</p>
<p>flickr.photos.geo.photosForLocation方法并不能返回任何值</p>
<p>可以用的是方法flickr.photos.search：</p>
<p>1.通过bbox来选定地理范围，每页返回250数据</p>
<p>2.输入某一点的经纬度和搜索半径（最大32km）</p>

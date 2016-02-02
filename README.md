# Scrapy Projects

## JikeEdu Branch

### 03 Introduction to Scrapy
Crawl from top250 movies from movie.douban.com/top250. Extract title, description, rating and quote for each movie.

#### Procedure
* scrapy startproject xxx
* scrapy genspider xxxx
* define custom spider
* define custom item
* edit pipelines for post-processing data[optional]
* 

### 03 Scrapy And MongoDB
* MongoDB - a database 
* mongovue - visualization for MongoDB
* pymongo
* Use pipelines to store crawled data into MongoDB


## Bug Fix
1. scrapy [boto] ERROR: Caught exception reading instance data URLError: <urlopen error [Errno 10051]
  * 参考了下面两个链接，解决方法一样，通过在settings.py中加如下配置
  {{{DOWNLOAD_HANDLERS : {
    's3': None,
}
}}}
  * [http://blog.csdn.net/liyuetao680/article/details/48313313]
  * [stackoverflow](http://stackoverflow.com/questions/32132482/scrapy-shell-error)



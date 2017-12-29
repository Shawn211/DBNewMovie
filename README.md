# DBNewMovie
Python爬虫使用Scrapy框架抓取了豆瓣新片榜内的电影信息</br>

初始化创建Scrapy工程：        scrapy startproject dbnewmovie</br>
并创建spider：               scrapy genspider movie movie.douban.com/chart</br>

目录结构：</br>
├── scrapy.cfg</br>
│</br>
└── dbnewmovie</br>
....├── items.py</br>
....├── middlewares.py</br>
....├── pipelines.py</br>
....├── settings.py</br>
....├── __init__.py</br>
....│</br>
....└── spiders</br>
........├── movie.py</br>
........└── __init__.py</br>

在dbnewmovie/items中创建了四个field</br>
分别存储电影名字、电影评分、点评人数、电影链接</br>
最后将其写入movie文件</br>

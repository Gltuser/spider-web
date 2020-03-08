# spider-web

这是一个简易的爬取数据并制作可视化大屏，并写入本地的html的项目。

首先，从腾讯疫情动态（网址：https://news.qq.com/zt2020/page/feiyan.htm#/)
、百度疫情热搜（网址：https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1）
上爬取疫情相关信息并存入本地的MySQL数据库中，爬虫见spider.py和spider_for_baidu_hot.py。

然后，使用flask搭建web，并使用echarts绘制交互式的地理信息图、疫情趋势图等，效果图如下。

![image](https://github.com/Gltuser/spider-web/raw/master/show.jpg)

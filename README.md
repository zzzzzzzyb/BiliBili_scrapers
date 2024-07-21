# BiliBili爬虫

## links_1.txt

scrapy爬虫爬取

https://www.bilibili.com/read/cv30820376

https://www.bilibili.com/read/cv30820468

https://www.bilibili.com/read/cv30820561

得到，其中内容为截至2024-2-4B站所有100万粉丝以上Up主主页URL。

## links.py
scrapy爬虫体

## main.py

selenium获取links_1.txt中所有Up主全部投稿视频的BV号
通过BV号获取视频信息可调用B站api。

https://api.bilibili.com/x/web-interface/view

https://api.bilibili.com/x/web-interface/archive/like

https://api.bilibili.com/x/web-interface/coin/add

https://api.bilibili.com/medialist/gateway/coll/resource/deal

详见：https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/README.md

## getTops.py

获得B站当日所有分区热榜

## getOid.py
通过BV号获得视频oid，即B站视频的唯一标识。

## getDanmaku.py

通过对接口
https://api.bilibili.com/x/v2/dm/web/history/seg.so 的解析获得B站视频历史弹幕。

该api接收三个参数，本代码中已将type参数写死为1，代表视频弹幕；

oid参数为视频oid；

date参数为日期，YYYY-MM-DD格式。

B站对较老的视频的弹幕存储方式与较新的视频不同，建议应用于较新的视频，并将date参数设为当前日期,否则难以获得符合预期的结果。

## dm.proto

详见
https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/grpc_api/bilibili/community/service/dm/v1/dm.proto

## dm_pb2.py

使用protoc 5.27.2将dm.proto转换而得。请确保protobuf版本也为5.27.2.也可自行重新转换，但需保证protobuf与protoc版本相同。

## getBangumi.py

获得B站几乎全部番剧基本信息。

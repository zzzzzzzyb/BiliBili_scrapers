import datetime
from time import sleep

import requests
import google.protobuf.text_format as text_format
from getOid import get_video_cid
import dm_pb2 as Danmaku

import re

def getDanmaku(bv,startdate):
    oid = get_video_cid(bv)
    print(oid)
    # 爬取开始日期和结束日期范围内的弹幕
    resList = []
    tmp_res_list =[]
    url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={oid}&date={startdate}'
    headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'cookie': 'buvid3=4A0421A6-20F9-29DB-5D32-D6673056E9BF31924infoc; b_nut=1718016531; _uuid=1D65FAE2-6A86-46C3-610105-9BECC2B3859F32633infoc; enable_web_push=DISABLE; header_theme_version=CLOSE; rpdid=0zbfVGbwlN|emrFgv9m|34P|3w1SgCAz; CURRENT_QUALITY=80; fingerprint=6f18e1821ef7aaf9e9dafaa65e4fb2e1; buvid_fp_plain=undefined; buvid4=540E941F-F4C2-4E75-25A7-6135D0C343ED32675-024061010-%2BoqH4JWpvfIOkbWcOWAb2uGZwrqLAPoF9BKMMtVS3dbhvHdeJA0PPF4D%2BJlhZeVU; LIVE_BUVID=AUTO5017193226842845; is-2022-channel=1; CURRENT_BLACKGAP=0; PVID=1; home_feed_column=5; hit-dyn-v2=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjE0NjcyMzgsImlhdCI6MTcyMTIwNzk3OCwicGx0IjotMX0.XIBiwiBlnRMumxaqDMjY-dTK9NqTtPt7zaLy0zKLX8M; bili_ticket_expires=1721467178; SESSDATA=abd89283%2C1736772489%2Cdb54b%2A71CjBa5SEhrc0QNAor46z5YTGVsYIdX6Cw7C_fusmVOJc-AcCAUEv-R3Y_zXrXai4cfSYSVnhKQTAzQ1VZX3lnQUpqcVduTUI4RmRyTlZNMkRUejhEN1hzcjZtcW5LZUtQWUFBakVaaDhvU3hWOWl0Y25DVERsZVFDczRQMEROYTNMZ24tQTNuX2RnIIEC; bili_jct=63d0c94fb484f15a8371b9d02bfc15e7; DedeUserID=48002287; DedeUserID__ckMd5=be7b54b6f8c02f7a; sid=6r3vt0kx; CURRENT_FNVAL=4048; share_source_origin=QQ; bsource=share_source_qqchat; buvid_fp=6f18e1821ef7aaf9e9dafaa65e4fb2e1; bp_t_offset_48002287=955157132712345600; b_lsid=E67BA4EB_190C9DFA6A6; browser_resolution=1612-209'
        }
    resp = requests.get(url,headers=headers)
    data = resp.content
    danmaku_seg = Danmaku.DmSegMobileReply()
    danmaku_seg.ParseFromString(data)
    for danmakus in range(0,len(danmaku_seg.elems)):
        res = text_format.MessageToString(danmaku_seg.elems[danmakus],as_utf8=True)
        pattern = r'content:(.*?)\n'
        tmp_res_list.append(re.findall(pattern, res, re.DOTALL)[0].replace('"', ''))
    resList.extend(tmp_res_list)

    return resList



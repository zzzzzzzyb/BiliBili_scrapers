import json
import requests

def get_video_cid(bvid):
    url = f'https://api.bilibili.com/x/web-interface/view?bvid={bvid}'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    html = r.text
    if html:
        _json = json.loads(html)
        cid = _json['data'].get('cid')
        return cid



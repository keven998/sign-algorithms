import requests
import time
import uuid
import base64
import hashlib
from urllib import parse

# udid参数: android_id+MacAddress+Model+Manufacturer
# android_id：88896b9e25fe8a4c
# MacAddress:32:DF:7A:24:E7:18
# Model:Nexus 6P
# Manufacturer:null
# udid=hashlib.md5(b"88896b9e25fe8a4c32:DF:7A:24:E7:18Nexus 6Pnull").hexdigest().upper()

# devId: imei+mac
# imei:867532812546220
# mac:32:DF:7A:24:E7:18
# devId=hashlib.md5(b'86753281254622032:DF:7A:24:E7:18').hexdigest().upper()

def get_sign(path,uid,s_time):
    md5str=f'url={path}unique_id={uid}version=7.2.70timestamp={s_time}4O230P1eeOixfktCk2B0K8d0PcjyPoBC'
    sign=hashlib.md5(md5str.encode()).hexdigest()
    return sign

if __name__=="__main__":
	url=f"http://b-api.ins.miaopai.com/1/search/media.json?count=20&page=1&key={parse.quote('飞天')}"
	uid=str(uuid.uuid1())
	s_time=int(time.time())
	path=url.split("?")[0].split(".com")[1]
	sign=get_sign(path,uid,s_time)
	headers={"cp-os": "android",
	"cp-abid": "1-10,2-1",
	"cp-sign": sign,
	"cp-sver": "5.1.1",
	"cp-appid": "424",
	"cp-uniqueId": uid,
	"cp-time": str(s_time),
	"cp-uuid": uid,
	"cp-channel": "huawei_market",
	"cp_kid": "0",
	"cp-vend": "miaopai",
	"cp-ver": "7.2.70",
	"Host": "b-api.ins.miaopai.com",
	"Connection": "Keep-Alive",
	"Accept-Encoding": "gzip",
	"User-Agent": "okhttp/3.3.1"}

	r=requests.get(url=url,headers=headers)
	data=base64.b64encode(r.content).decode()
	b=requests.post(url="http://127.0.0.1:8887/decode",data=data)
	print(b.json()["result"][1])


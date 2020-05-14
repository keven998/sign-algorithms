# 简介
##### 逆向Android app获取或调用签名算法。

app | 版本 | 参数 | 说明 | 时间
-|-|-|- | -
美拍 | 7.9.5 | sig和sigTime | | 
梨视频 | 6.7.2 | X-Client-Hash | | 
链家 | 9.12.0 | Authorization | | 
秒拍 | 7.2.68 | sign和response解密 | 调用libte.so，集成在HttpSo:https://github.com/heyaug/HttpSo | 2020.5.7 
小红书 | - | sign | | 
抖音 | 10.9.0 | x-gorgon和X-Khronos | 调用libcms.so生成0404开头的x-gorgon，集成在HttpSo:https://github.com/heyaug/HttpSo | 2020.5.9 

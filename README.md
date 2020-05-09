# 简介
##### 逆向Android app获取签名或加密算法。

#### 美拍
##### 版本-7.9.5
##### url参数中sig和sigTime

#### 梨视频
##### 版本-6.7.2
##### headers里X-Client-Hash

#### 链家
##### 版本-9.12.0
##### headers的Authorization

#### 秒拍
##### 版本-7.2.68
##### 2020.5.7 更新sign和response解密
##### response解密
##### 调用libte.so的Decode方法，已集成在HttpSo项目中
##### https://github.com/heyaug/HttpSo

#### 小红书
##### 版本-
##### url里的sign，听说sheild很难

#### 抖音
##### 版本-10.9.0
##### 2020.5.9 从抖音10.9.0更新libcms.so
##### 生成0404开头的gorgon
##### 增加示例
##### https://github.com/heyaug/HttpSo
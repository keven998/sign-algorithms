# 简介
##### 通过逆向Android app获取签名或加密算法。

### App列表

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
##### 一些参数生成方式
##### 2020.5.7 更新sign和response解密
##### response解密调用libte.so的Decode方法，已集成在HttpSo项目中
##### https://github.com/heyaug/HttpSo

#### 小红书
##### 版本-
##### url里的sign，听说sheild很难

#### 抖音
##### 版本-10.1.0
##### 已解决gorgon和设备注册，xlog
##### https://github.com/heyaug/HttpSo
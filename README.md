## UIT
`appium` + `unitTest`框架，`po`模式设计


### 安装使用
* [Python3.7](https://www.python.org/downloads/release/python-378/)
* [Appium Desktop Client](https://github.com/appium/appium-desktop)
* [Android SDK tools package](https://dl.google.com/android/repository/commandlinetools-mac-6609375_latest.zip)
* [Android Debug Bridge version 1.0.41](https://developer.android.google.cn/studio/)
* Android API Version 29.0.1 -> android 10
* 团油app V5.2.2 ```运行脚本前，请安装好```
* Android 6.0.1、10.0 测试通过

以上配置完成后，请运行以下脚本配置环境:

```bash
# iOS tools
$ brew install usbmuxd
$ brew install ideviceinstaller
$ brew install ios-webkit-debug-proxy # webview
$ npm -version
> 6.14.4

# macaca driver
# 安装有 TEAM_ID 的 macaca-ios
$ DEVELOPMENT_TEAM_ID=TEAM_ID npm i macaca-ios -g
$ brew install gradle
$ npm i macaca-android -g
$ npm i macaca-electron -g
$ npm i macaca-chrome -g
$ npm i -g macaca-cli
$ macaca doctor

# python 虚拟环境
$ cd uit
$ rm -rf venv
$ virtualenv --no-site-packages venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

### 运行
1. 请启动`Appium Desktop App`；
2. 请确认 `__conf.py`中，客户端配置参数是否与测试机一致；
3. 请确认 `__conf.py`中，数据库配置参数是否与测试机运行环境一致；
4. 请确认命令行中 `adb devices` 正常运行，并显示设备信息;
5. 如果3运行不正常，请检查测试机是否开启开发者模式，并打开`usb`调试模式，如果仍然不行，请重启电脑；
6. 测试过程中，请开启测试机的充电不锁屏选项；

### 注意
1. 先去`user.yaml`文件里去改成自己的手机号；

### run
点击图片查看视频

[![IMAGE ALT TEXT](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1593436429719&di=1b25f5c0afa711a42c48df138a92f288&imgtype=0&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D242481744%2C930275026%26fm%3D214%26gp%3D0.jpg)](https://v.youku.com/v_show/id_XNDczMzU1MTEwMA==.html "CameraMaster")

## ATM
appium + unitTest框架，po模式

### 安装使用
* Python3.7
* Appium Desktop Client 1.9.1
* Appium-Python-Client 0.50 
* Android Debug Bridge version 1.0.41
* Android API Version 29.0.1
* 被测试的app ```运行脚本前，请安装好```
* P30 pro 真机 Android 10 测试通过
* mumu 模拟器 huawei mate10 pro  Android 6.0.1 测试通过

以上配置完成后，请运行以下脚本配置环境:

```bash
# iOS tools
brew install libimobiledevice
brew install ideviceinstaller

# python 虚拟环境
rm -rf venv
virtualenv --no-site-packages venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### 运行
1. 请启动Appium Desktop App；
2. 请确认 `__conf.py`中，客户端配置参数是否与测试机一致；
3. 请确认 `__conf.py`中，数据库配置参数是否与测试机运行环境一致；
4. 请确认命令行中 `adb devices` 正常运行，并显示设备信息;
5. 如果3运行不正常，请检查测试机是否开启开发者模式，并打开usb调试模式，如果仍然不行，请重启电脑；
6. 测试过程中，请开启测试机的充电不锁屏选项；

### 业务代码
所有的业务代码都放到`module`模块当中了，如果想要使用本框架，只需要在`module`中扩展，相应的页面和封装流程即可。

### 注意
1. 先去`user.yaml`文件里去改成自己的手机号；
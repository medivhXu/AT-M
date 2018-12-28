# ！/usr/bin/env python3

import abc


class DriverBehavior(metaclass=abc.ABCMeta):
    def __init__(self):
        self.driver = None

    @abc.abstractmethod
    def swipe_up(self, driver):
        """左滑"""
        raise NotImplementedError

    @abc.abstractmethod
    def swipe_down(self,driver):
        """下滑"""
        raise NotImplementedError

    @abc.abstractmethod
    def swipe_left(self,driver):
        """上滑"""
        raise NotImplementedError

    @abc.abstractmethod
    def swipe_right(self,driver):
        raise NotImplementedError

    @abc.abstractmethod
    def find_element(self,driver):
        raise NotImplementedError

    @abc.abstractmethod
    def find_elements_(self):
        raise NotImplementedError

    @abc.abstractmethod
    def implicitly_wait(self):
        raise NotImplementedError

    @abc.abstractmethod
    def compel_waiting(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_title(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_alert_text(self):
        raise NotImplementedError

    @abc.abstractmethod
    def ios_sys_alert(self):
        raise NotImplementedError

    def find_accessibility_id(self):
        raise NotImplementedError

    @abc.abstractmethod
    def find_element_by_ios_predicate_(self):
        """支持原生，可以做比较或模糊操作
            栗子：'name == "guide openMode"'
                'abel LIKE '*uide openMode'
                'abel LIKE '?uide openMode'
        """
        raise NotImplementedError

    @abc.abstractmethod
    def find_elements_by_ios_predicate_(self):
        """支持原生，可以做比较或模糊操作
            栗子：'name == "guide openMode"'
                'abel LIKE '*uide openMode'
                'abel LIKE '?uide openMode'
                包含某个字符串，如：label CONTAINS '测试'
                以某个字符串开头，如：label BEGINSWITH '420'
                以某个字符串结束，如：label ENDSWITH '班级群'
        """
        raise NotImplementedError

    @abc.abstractmethod
    def scroll_el_to_el(self):
        """从el1 滚动到 el2"""
        raise NotImplementedError

    @abc.abstractmethod
    def drag_el_to_el(self):
        """从el1 拖到 el2"""
        raise NotImplementedError

    @abc.abstractmethod
    def tap_(self):
        """手指点击
        duration_time：按住时间（ms）
        driver.tap([(x,y),(x1,y1)],500)"""
        raise NotImplementedError

    @abc.abstractmethod
    def fast_sliding(self):
        """按住A点后快速滑动至B点"""
        raise NotImplementedError

    @abc.abstractmethod
    def pinch_element(self):
        """在元素上模拟双指捏（缩小操作）"""
        raise NotImplementedError

    @abc.abstractmethod
    def zoom_element(self):
        """放大操作"""
        raise NotImplementedError

    @abc.abstractmethod
    def reset_app(self):
        """重置应用"""
        raise NotImplementedError

    @abc.abstractmethod
    def press_keycode_by_android(self):
        """发送按键码
        KEYCODE_CALL        拨号键       5
        KEYCODE_ENDCALL     挂机键       6
        KEYCODE_HOME        按键Home     3
        KEYCODE_MENU        菜单键       82
        KEYCODE_BACK        返回键       4
        KEYCODE_SEARCH      搜索键       84
        KEYCODE_CAMERA      拍照键       27
        KEYCODE_FOCUS       拍照对焦键    80
        KEYCODE_POWER       电源键       26
        KEYCODE_NOTIFICATION 通知键      83
        KEYCODE_MUTE        话筒静音键    91
        KEYCODE_VOLUME_MUTE 扬声器静音键  164
        KEYCODE_VOLUME_UP   音量增加键    24
        KEYCODE_VOLUME_DOWN 音量减小键    25
        """
        raise NotImplementedError

    def long_press_keycode_by_android(self):
        """发送一个长按的按键码(长按某键)"""
        raise NotImplementedError

    def get_activity(self):
        """获取当前的 activity"""
        raise NotImplementedError

    def wait_activity_(self):
        """等待指定的 activity 出现直到超时，interval 为扫描间隔 1 秒 即每隔几秒获取一次当前的 activity"""
        raise NotImplementedError

    def background_app_(self):
        """后台运行 app 多少秒"""
        raise NotImplementedError

    def is_app_installed_(self):
        """检查 app 是否有安装 返回 True or False"""
        raise NotImplementedError

    @abc.abstractmethod
    def install_app_(self):
        """安装 app,app_path 为安装包路径"""
        raise NotImplementedError

    @abc.abstractmethod
    def remove_app_(self):
        raise NotImplementedError

    @abc.abstractmethod
    def launch_app_(self):
        """启动app，注只有设置autoLaunch=false时才会生效"""
        raise NotImplementedError

    @abc.abstractmethod
    def close_app_(self):
        """据说会报错"""
        raise NotImplementedError

    def start_activity_by_android(self):
        raise NotImplementedError

    def lock_screen_by_ios(self):
        """锁屏一段时间 iOS 专有"""
        raise NotImplementedError

    def shake_(self):
        """摇一摇手机"""
        raise NotImplementedError

    def open_notifications_by_android(self):
        """打系统通知栏(仅支持 atm 18 以上的安卓系统)"""
        raise NotImplementedError

    def network_connection_by_android(self):
        """返回网络类型 数值"""
        raise NotImplementedError

    def set_network_connection_by_android(self, connection_type):
        """设置网络类型"""
        raise NotImplementedError

    def available_ime_engines_by_android(self):
        """返回安卓设备可用的输入法"""
        raise NotImplementedError

    def toggle_location_services_by_android(self):
        """打开模拟定位"""
        raise NotImplementedError

    def set_location_by_android(self):
        """设置设备的经纬度"""
        raise NotImplementedError

    def get_screenshot_as_base64_(self):
        """获取当前元素的截图为 Base64 编码的字符串"""
        raise NotImplementedError

    def get_screenshot_as_png_(self):
        raise NotImplementedError

    def get_screenshot_as_file_(self):
        raise NotImplementedError

    def screenshot_(self):
        raise NotImplementedError

    def get_current_url(self):
        """获取当前页面的网址"""
        raise NotImplementedError

    def get_page_source(self):
        """获取当前页面的源"""
        raise NotImplementedError

    def close_(self):
        """关闭当前窗口"""
        raise NotImplementedError

    def quit_(self):
        """退出脚本运行并关闭每个相关的窗口连接"""
        raise NotImplementedError

    def get_context(self):
        """返回当前会话中的上下文，使用后可以识别 H5 页面的控件"""
        raise NotImplementedError

    def get_contexts(self):
        """获取可用的上下文"""
        raise NotImplementedError

    def get_current_context(self):
        """返回当前会话的当前上下文"""
        raise NotImplementedError

    def get_app_strings(self):
        """获取app 应用字符串，多语言文本"""
        raise NotImplementedError

    def send_click_event(self, key):
        """发送按键事件"""
        raise NotImplementedError

    def get_current_package(self):
        """获取当前包名，only Android"""
        raise NotImplementedError

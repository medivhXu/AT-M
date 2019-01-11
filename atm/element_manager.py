# !/uer/bin/env python3

import time
import os
import unittest
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from atm.log import logged

__dir__ = os.path.dirname(os.path.abspath(__file__))


class MobileDriver(unittest.TestCase):
    def setUp(self):
        self.driver = None

    def tearDown(self):
        pass

    @logged
    def swipe_up(self, proportion_screen_start=0.75, proportion_screen_end=0.25, s_time=500, n=1):
        """
        向上滑动
        """
        if proportion_screen_start < proportion_screen_end:
            raise ValueError("向上滑动数据错误，proportion_screen_start必须大于proportion_screen_end")
        screen_size = self.driver.get_window_size()
        f_x1 = screen_size['width'] * 0.5
        f_y1 = screen_size['height'] * proportion_screen_start
        s_y2 = screen_size['height'] * proportion_screen_end
        for i in range(n):
            self.driver.swipe(f_x1, f_y1, f_x1, s_y2, s_time)
            self.compel_waiting()

    @logged
    def swipe_down(self, proportion_screen_start=0.25, proportion_screen_end=0.75, s_time=500, n=1):
        """
        向下滑动
        """
        if proportion_screen_start > proportion_screen_end:
            raise ValueError("向上滑动数据错误，proportion_screen_start必须小于proportion_screen_end")
        screen_size = self.driver.get_window_size()
        f_x1 = screen_size['width'] * 0.5
        f_y1 = screen_size['height'] * proportion_screen_start
        s_y2 = screen_size['height'] * proportion_screen_end
        for i in range(n):
            self.driver.swipe(f_x1, f_y1, f_x1, s_y2, s_time)
            self.compel_waiting()

    @logged
    def swipe_left(self, proportion_screen_start=0.75, proportion_screen_end=0.05, n=1, s_time=500):
        """
        向左滑动
        """
        if proportion_screen_start < proportion_screen_end:
            raise ValueError("向上滑动数据错误，proportion_screen_start必须大于proportion_screen_end")
        screen_size = self.driver.get_window_size()
        f_y1 = screen_size['height'] * 0.5
        f_x1 = screen_size['width'] * proportion_screen_start
        s_x2 = screen_size['width'] * proportion_screen_end
        for i in range(n):
            self.driver.swipe(f_x1, f_y1, s_x2, f_y1, s_time)
            self.compel_waiting()

    @logged
    def swipe_right(self, proportion_screen_start=0.05, proportion_screen_end=0.75, s_time=500, n=1):
        """
        向右滑动
        s_time:毫秒
        """
        if proportion_screen_start > proportion_screen_end:
            raise ValueError("向上滑动数据错误，proportion_screen_start必须小于proportion_screen_end")
        screen_size = self.driver.get_window_size()
        f_y1 = screen_size['height'] * 0.5
        f_x1 = screen_size['width'] * proportion_screen_start
        s_x2 = screen_size['width'] * proportion_screen_end
        for i in range(n):
            self.driver.swipe(f_x1, f_y1, s_x2, f_y1, s_time)
            self.compel_waiting()

    @logged
    def android_element_wait(self, by, value, secs=10):
        """
        Waiting for an element to display.
        """
        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NoSuchElementException(
                "Not find element, Please check the syntax error.")

    @logged
    def find_element_(self, css):
        if "=>" not in css:
            by = "css"
            value = css
            self.android_element_wait(by, css)
        else:
            by = css.split("=>")[0]
            value = css.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "Grammatical errors,reference: 'id=>useranme'.")
            self.android_element_wait(by, value)

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        elif by == "tag_name":
            element = self.driver.find_element_by_tag_name(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    @logged
    def find_elements_(self, el):
        if "=>" not in el:
            by = "css"
            value = el
            self.android_element_wait(by, el)
        else:
            by = el.split("=>")[0]
            value = el.split("=>")[1]
            if by == "" or value == "":
                raise NameError(
                    "Grammatical errors,reference: 'id=>useranme'.")
            self.android_element_wait(by, value)

        if by == "id":
            elements = self.driver.find_elements_by_id(value)
        elif by == "name":
            elements = self.driver.find_elements_by_name(value)
        elif by == "class":
            elements = self.driver.find_elements_by_class_name(value)
        elif by == "link_text":
            elements = self.driver.find_elements_by_link_text(value)
        elif by == "xpath":
            elements = self.driver.find_elements_by_xpath(value)
        elif by == "css":
            elements = self.driver.find_elements_by_css_selector(value)
        elif by == "tag_name":
            elements = self.driver.find_elements_by_tag_name(value)
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return elements

    @logged
    def implicitly_wait(self, sec=0.001):
        self.driver.implicitly_wait(sec)

    @logged
    def compel_waiting(self, sec=0.001):
        if not isinstance(sec, (float, int)):
            raise ValueError("sec must be a number!")
        time.sleep(sec)

    @logged
    def click(self, css):
        el = self.find_element_(css)
        el.click()

    @logged
    def send_keys(self, css, *text):
        self.find_element_(css).clear()
        self.find_element_(css).send_keys(text)

    @logged
    def get_title(self):
        return self.driver.title()

    @logged
    def get_alert_text(self):
        return self.driver.switch_to.alert.text()

    @logged
    def ios_sys_alert(self, n=1):
        for i in range(n):
            self.driver.switch_to.alert.accept()
            self.compel_waiting()

    @logged
    def find_accessibility_id(self, element_id, sec=10):
        WebDriverWait(self.driver, sec, 1).until(EC.presence_of_element_located((By.ACCESSIBILITY_ID, element_id)))
        return self.driver.find_element_by_accessibility_id(element_id)

    @logged
    def find_element_by_ios_predicate_(self, predicate_string, sec=10):
        """支持原生，可以做比较或模糊操作
            栗子：'name == "guide openMode"'
                'abel LIKE '*uide openMode'
                'abel LIKE '?uide openMode'
        """
        WebDriverWait(self.driver, sec, 0.5).until(EC.presence_of_element_located((By.IOS_PREDICATE, predicate_string)))
        return self.driver.find_element_by_ios_predicate(predicate_string)

    @logged
    def find_elements_by_ios_predicate_(self, predicate_string, sec=10):
        """支持原生，可以做比较或模糊操作
            栗子：'name == "guide openMode"'
                'abel LIKE '*uide openMode'
                'abel LIKE '?uide openMode'
                包含某个字符串，如：label CONTAINS '测试'
                以某个字符串开头，如：label BEGINSWITH '420'
                以某个字符串结束，如：label ENDSWITH '班级群'
        """
        WebDriverWait(self.driver, sec, 0.5).until(EC.presence_of_element_located((By.IOS_PREDICATE, predicate_string)))
        return self.driver.find_elements_by_ios_predicate(predicate_string)

    @logged
    def scroll_el_to_el(self, el1, el2):
        """从el1 滚动到 el2"""
        self.driver.scroll(el1, el2)

    @logged
    def drag_el_to_el(self, el1, el2):
        """从el1 拖到 el2"""
        self.driver.drag_and_drop(el1, el2)

    @logged
    def tap_(self, coordinates_tuple, n=1, duration_time=None):
        """手指点击
        duration_time：按住时间（ms）
        driver.tap([(x,y),(x1,y1)],500)"""
        for i in range(n):
            self.driver.tap(coordinates_tuple, duration_time)
            self.compel_waiting()

    @logged
    def fast_sliding(self, start_x, start_y, end_x, end_y):
        """按住A点后快速滑动至B点"""
        self.driver.flick(start_x, start_y, end_x, end_y)

    @logged
    def pinch_element(self, el, percent=200, steps=50):
        """在元素上模拟双指捏（缩小操作）"""
        self.driver.pinch(el, percent, steps)

    @logged
    def zoom_element(self, el, percent=200, steps=50):
        """放大操作"""
        self.driver.zoom(el, percent, steps)

    @logged
    def reset_app(self):
        """重置应用"""
        self.driver.reset()

    @logged
    def press_keycode_by_android(self, keycode, metastate=None):
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
        self.driver.press_keycode(keycode, metastate)

    @logged
    def long_press_keycode_by_android(self, keycode, metastate=None):
        """发送一个长按的按键码(长按某键)"""
        self.driver.long_press_keycode(keycode, metastate)

    @logged
    def get_activity(self):
        """获取当前的 activity"""
        return self.driver.current_activity()

    @logged
    def wait_activity_(self, activity, timeout, interval=1):
        """等待指定的 activity 出现直到超时，interval 为扫描间隔 1 秒 即每隔几秒获取一次当前的 activity
        返回的 True 或 False"""
        return self.driver.wait_activity(activity, timeout, interval)

    @logged
    def background_app_(self, sec):
        """后台运行 app 多少秒"""
        self.driver.background_app(sec)

    @logged
    def is_app_installed_(self, bundle_id):
        """检查 app 是否有安装 返回 True or False"""
        self.driver.is_app_installed(bundle_id)

    @logged
    def install_app_(self, app_path):
        """安装 app,app_path 为安装包路径"""
        self.driver.install_app(app_path)

    @logged
    def remove_app_(self, app_id):
        self.driver.remove_app(app_id)

    @logged
    def launch_app_(self):
        """启动app，注只有设置autoLaunch=false时才会生效"""
        self.driver.launch_app()

    @logged
    def close_app_(self):
        """据说会报错"""
        self.driver.close_app()

    @logged
    def start_activity_by_android(self, app_package, app_activity, **opt):
        self.driver.start_activity(app_package, app_activity, **opt)

    @logged
    def lock_screen_by_ios(self, sec):
        """锁屏一段时间 iOS 专有"""
        self.driver.lock(sec)

    @logged
    def shake_(self):
        """摇一摇手机"""
        self.driver.shake()

    @logged
    def open_notifications_by_android(self):
        """打系统通知栏(仅支持 atm 18 以上的安卓系统)"""
        self.driver.open_notifications()

    @logged
    def network_connection_by_android(self):
        """返回网络类型 数值"""
        return self.driver.network_connection()

    @logged
    def set_network_connection_by_android(self, connection_type):
        """设置网络类型"""
        from appium.webdriver.connectiontype import ConnectionType
        if connection_type not in (0, 1, 2, 4, 6):
            if connection_type == 0:
                self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
            elif connection_type == 1:
                self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
            elif connection_type == 2:
                self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
            elif connection_type == 4:
                self.driver.set_network_connection(ConnectionType.DATA_ONLY)
            elif connection_type == 6:
                self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
            else:
                raise ValueError("参数错误，connection_type :{}".format(connection_type))
        else:
            raise ValueError("参数必须在0，1，2，4，6中选择！")

    @logged
    def available_ime_engines_by_android(self):
        """返回安卓设备可用的输入法"""
        return self.driver.available_ime_engines()

    @logged
    def toggle_location_services_by_android(self):
        """打开模拟定位"""
        return self.driver.toggle_location_services()

    @logged
    def set_location_by_android(self, latitude, longitude, altitude):
        """设置设备的经纬度"""
        self.driver.set_location(latitude, longitude, altitude)

    @logged
    def get_tar_property(self, el):
        """返回元素的 tagName 属性 经实践返回的是 class name"""
        return self.find_element_(el).tag_name()

    @logged
    def get_element_text(self, el):
        """返回元素的文本值"""
        return self.find_element_(el).text()

    @logged
    def get_attribute(self):
        pass

    @logged
    def is_selected(self, el):
        """返回元素是否选择。可以用来检查一个复选框或单选按钮被选中。"""
        return self.find_element_(el).is_selected()

    @logged
    def is_enabled(self, el):
        """返回元素是否可用 True of False"""
        return self.find_element_(el).is_enable()

    @logged
    def get_element_size(self, el):
        """获取元素的大小(高和宽)"""
        return self.find_element_(el).size()

    @logged
    def get_location(self, el, x, y):
        """获取元素左上角的坐标"""
        _x = self.find_element_(el).location.get(x)
        _y = self.find_element_(el).location.get(y)
        return _x, _y

    @logged
    def get_screenshot_as_base64_(self):
        """获取当前元素的截图为 Base64 编码的字符串"""
        return self.driver.screenshot_as_base64()

    @logged
    def get_screenshot_as_png_(self):
        return self.driver.screenshot_as_png()

    @logged
    def get_screenshot_as_file_(self, filename):
        return self.driver.get_screenshot_as_file(filename)

    @logged
    def screenshot_(self, file_name='screenshot_img'):
        path = os.path.join(__dir__, ''.join(('../', file_name)))
        if file_name not in os.listdir(os.path.join(__dir__, '../')):
            os.mkdir(path)
        return self.driver.screenshot(path)

    @logged
    def get_current_url(self):
        """获取当前页面的网址。"""
        self.driver.current_url()

    @logged
    def get_page_source(self):
        """获取当前页面的源。"""
        self.driver.page_source()

    @logged
    def close_(self):
        """关闭当前窗口"""
        self.driver.close()

    @logged
    def quit_(self):
        """退出脚本运行并关闭每个相关的窗口连接"""
        self.driver.quit()

    @logged
    def get_context(self):
        """返回当前会话中的上下文，使用后可以识别 H5 页面的控件"""
        return self.driver.context()

    @logged
    def get_contexts(self):
        """获取可用的上下文"""
        return self.driver.contexts

    @logged
    def get_current_context(self):
        """返回当前会话的当前上下文"""
        return self.driver.current_context

    @logged
    def def_context(self):
        """切换至默认上下文"""
        pass

    @logged
    def get_app_strings(self):
        """获取app 应用字符串，多语言文本"""
        return self.driver.app_strings

    @logged
    def get_element_uiautomation_by_ios(self, uia_string):
        """返回当前会话的当前上下文。"""
        return self.driver.find_element_by_ios_uiautomation(uia_string)

    @logged
    def send_click_event(self, key):
        """发送按键事件"""
        self.driver.keyevent(keycode=key)

    @logged
    def get_current_package(self):
        """获取当前包名，only Android"""
        return self.driver.current_package()

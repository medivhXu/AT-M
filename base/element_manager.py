# !/uer/bin/env python3
"""
@author: Medivh Xu
@file: element_manager.py
@time: 2020-03-17 12:22
"""
import time
import os
import unittest
from appium.webdriver.common.mobileby import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from base.logged import logged, logger

__dir__ = os.path.dirname(os.path.abspath(__file__))


class MobileBy(By):
    IOS_UIAUTOMATION = '-ios uiautomation'
    ANDROID_UIAUTOMATOR = '-android uiautomator'
    ACCESSIBILITY_ID = 'accessibility id'


class BasePage:
    def __init__(self, driver):
        self.driver = driver

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
            time.sleep(0.5)

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
            time.sleep(0.5)

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
            time.sleep(0.5)

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
            time.sleep(0.5)

    def find_element(self, *loc, secs=10):
        try:
            el = WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(loc))
            return el
        except:
            logger.warning('页面未找到{}元素'.format(loc))

    def find_elements(self, *loc, secs=10):
        try:
            els = WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_all_elements_located(loc))
            return els
        except:
            logger.warning('页面未找到{}元素'.format(loc))

    def android_uiautomator(self, *loc, secs=10):
        try:
            el = WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located(loc))
            return el
        except:
            logger.warning('页面未找到{}元素'.format(loc))

    def always_allow_android(self, platform_version, number=5):
        if platform_version == '10':
            loc = ('xpath', "//*[@text='始终允许']")
        else:
            loc = ('xpath', "//*[@text='允许']")
        for i in range(number):
            try:
                e = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass

    def tap_(self, coordinates, n=1, duration_time=None):
        """手指点击
        duration_time：按住时间（ms）
        driver.tap([(x,y),(x1,y1)],500)
        """
        for i in range(n):
            self.driver.tap(coordinates, duration_time)
            time.sleep(0.5)

    def is_element(self, *loc):
        try:
            self.find_element(*loc)
        except NoSuchElementException as e1:
            logger.warning('没找到元素: {}'.format(e1))
            return False
        except TimeoutException as e2:
            logger.warning('没找到元素: {}'.format(e2))
            return False
        else:
            return True

    def send_keys(self, *loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self.driver, "_{}".format(loc))
            if click_first:
                self.driver.find_element(*loc).click()
            if clear_first:
                self.driver.find_element(*loc).clear()
                self.driver.find_element(*loc).send_keys(value)
        except AttributeError:
            logger.warning("{} 页面中未能找到 {} 元素".format(self.driver, loc))

    def is_toast_exist(self, text):
        try:
            toast_loc = (By.XPATH, "//*[@text='%s']" % text)
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located(toast_loc))
            return True
        except Exception as e:
            logger.warning("{} 页面中未能找到 {} 元素".format(self.driver, text))
            return False

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

    def hide_keyboard(self, key_name=None, key=None, strategy=None):
        self.driver.hide_keyboard(key_name, key, strategy)

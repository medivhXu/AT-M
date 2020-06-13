#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: android_keycode_enum.py
@time: 2020-04-09 18:34
"""

from enum import Enum


class AndroidKeyCodeEnum(Enum):
    CALL = 5             # 拨号键
    ENDCALL = 6          # 挂机键
    HOME = 3             # 按键Home
    MENU = 82            # 菜单键
    BACK = 4             # 返回键
    SEARCH = 84          # 搜索键
    CAMERA = 27          # 拍照键
    FOCUS = 80           # 拍照对焦键
    POWER = 26           # 电源键
    NOTIFICATION = 83    # 通知键
    MUTE = 91            # 话筒静音键
    VOLUME_MUTE = 164    # 扬声器静音键
    VOLUME_UP = 24       # 音量增加键
    VOLUME_DOWN = 25     # 音量减小键

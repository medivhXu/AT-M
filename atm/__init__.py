# ！/usr/bin/env python3

__author__ = "medivhXu"

__version__ = "1.0.0"

__email__ = "medivh_xu@outlook.com"

"""
1.0.0 version update:
* 设备管理
* 
"""


from atm.apps import Apps
from atm.devices import Android, Ios, IosSimulator
from exceptions.myexception import *
from atm.log import LOGGER, logged


@logged
def conn(platform=None, ip=None, capability=None):
    if not platform:
        cls = IosSimulator
    else:
        platform_dict = {'Android': Android, 'Ios': Ios}
        if str(platform).capitalize() in platform_dict:
            cls = platform_dict.get(str(platform).capitalize())
        else:
            raise MyException("未实现该平台！目前只实现：{}".format(platform_dict.keys()))
    c = cls(ip, capability)
    return c


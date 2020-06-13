#!/usr/bin/env python3
# encoding: utf-8
"""
@author: Medivh Xu
@file: __init__.py.py
@time: 2020-02-27 12:33
"""

import re
import os

from .yaml_manager import ConfYaml
from base.logged import logger, logged
from base.my_exception import *

DP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')


@logged
def conf_load(file_name):
    """
    读取配置文件，如果文件名包含文件后缀，则自动找到最近修改的文件
    :param file_name:
        示例: 'cases.yaml' or file point
    :return: type(obj)
    """
    if '../' in file_name:
        fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
        file_type = file_name.split('/')[-1].split('.')[-1]
        if 'yaml' == file_type:
            return ConfYaml(fp)
        else:
            raise FileTypeException("文件类型不匹配！")

    fp = os.path.join(DP, file_name)
    if os.path.isfile(fp):
        file_type = file_name.split('.')[-1]
        if 'yaml' == file_type:
            return ConfYaml(fp)
        else:
            raise FileTypeException("文件类型不匹配！")
    else:
        # 取最新修改的文件
        files = os.listdir(DP)
        file_name_split = file_name.split('.')
        if len(file_name_split) > 1:
            files_dict = {f: os.stat(os.path.join(DP, f)).st_mtime for f in files if
                          re.search('{}.*.{}'.format(file_name_split[0], file_name_split[-1]), f)}
        else:
            files_dict = {f: os.stat(os.path.join(DP, f)).st_mtime for f in files if
                          re.search('{}.*'.format(file_name_split[0]), f)}
        try:
            new_modify = max(zip(files_dict.values(), files_dict.keys()))[1]
            file_type = new_modify.split('.')[-1]
            fp = os.path.join(DP, new_modify)
            if 'yaml' == file_type:
                return ConfYaml(fp)
            else:
                raise FileTypeException("文件类型不匹配！")
        except ValueError:
            logger.error("文件名没匹配到，请确认是否存在该文件！")
            raise NameError("文件名没匹配到，请确认是否存在该文件！")

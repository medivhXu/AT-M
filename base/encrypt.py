# !/uer/bin/env python3
"""
@author: Medivh Xu
@file: encrypt.py
@time: 2020-03-23 12:22
"""
import hashlib


class Encryption(object):
    """对参数进行md5加密"""

    @staticmethod
    def md5(string: str) -> str:
        md = hashlib.md5()
        md.update(string.encode(encoding='utf-8'))
        _md5_msg = str(md.hexdigest())
        return _md5_msg


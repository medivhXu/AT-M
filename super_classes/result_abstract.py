# ！/usr/bin/env python3

import abc


class Result(metaclass=abc.ABCMeta):
    """测试结果鸡肋"""
    @abc.abstractmethod
    def save_html(self):
        raise NotImplementedError

    def save_excel(self):
        raise NotImplementedError

    @abc.abstractmethod
    def send_result_to_email(self):
        raise NotImplementedError

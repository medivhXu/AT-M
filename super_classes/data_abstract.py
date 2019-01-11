# ！/usr/bin/env python3

import abc


class SourceData(metaclass=abc.ABCMeta):
    """读取数据鸡肋"""
    @abc.abstractmethod
    def get_data(self):
        raise NotImplementedError

    @abc.abstractmethod
    def next_data(self):
        raise NotImplementedError

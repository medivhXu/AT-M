# ！/usr/bin/env python3
import abc


class Case(metaclass=abc.ABCMeta):
    """测试用力鸡肋"""
    @abc.abstractmethod
    def get_case(self, case_no):
        raise NotImplementedError

    @abc.abstractmethod
    def next_case(self, current_case_no):
        raise NotImplementedError

    @abc.abstractmethod
    def get_status(self, case_no):
        raise NotImplementedError

    @abc.abstractmethod
    def set_status(self, case_no):
        raise NotImplementedError

# ！/usr/bin/env python3
import abc


class Case(metaclass=abc.ABCMeta):
    def __init__(self, case):
        self.case = case
        self.status = False

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

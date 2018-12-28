# ！/usr/bin/env python3

import abc


class Data(metaclass=abc.ABCMeta):
    def __init__(self):
        self.data = ()

    @abc.abstractmethod
    def get_data(self):
        raise NotImplementedError

    @abc.abstractmethod
    def next_data(self):
        raise NotImplementedError

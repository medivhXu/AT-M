# ！/usr/bin/env python3

import abc


class DB(metaclass=abc.ABCMeta):
    def __init__(self):
        self.db = None

    @abc.abstractmethod
    def select(self, sql):
        raise NotImplementedError

    @abc.abstractmethod
    def insert(self, sql):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, sql):
        raise NotImplementedError

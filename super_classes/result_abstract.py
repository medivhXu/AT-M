# ！/usr/bin/env python3

import abc


class Result(metaclass=abc.ABCMeta):
    def __init__(self):
        self.result = None

    @abc.abstractmethod
    def save_html(self):
        raise NotImplementedError

    def save_excel(self):
        raise NotImplementedError

    @abc.abstractmethod
    def send_result_to_email(self):
        raise NotImplementedError

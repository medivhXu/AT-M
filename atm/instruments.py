#!/usr/bin/env python3

from super_classes.commond import Command


class Instruments(Command):
    def __init__(self):
        super(Instruments, self).__init__()

    def connect(self):
        pass

    def disconnect(self):
        pass

    def kill_port(self, port):
        raise NotImplementedError

    def check_port(self, port):
        raise NotImplementedError

    def start_appium(self, add, port, bootstrap_port, chrome_port, udid):
        raise NotImplementedError

    def show_sdk(self):
        raise NotImplementedError

#!/usr/bin/env python3


class MyException(Exception):
    def __init__(self, msg):
        super().__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg


class AdbEnvironmentException(MyException):
    pass


class AdbConnectException(MyException):
    pass


class InstrumentsEnvironmentException(MyException):
    pass


class AppFileNotFoundException(MyException):
    pass


class AppFileNotOnlyException(MyException):
    pass


class PlatFormException(MyException):
    pass


class DeviceNotFoundException(MyException):
    pass


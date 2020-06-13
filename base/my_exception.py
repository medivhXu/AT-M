#!/usr/bin/env python3
"""
@author: Medivh Xu
@file: my_exception.py
@time: 2020-02-27 12:22
"""


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


class AppFileNotMatchException(MyException):
    pass


class PlatFormException(MyException):
    pass


class DevicesException(MyException):
    pass


class DeviceNotFoundException(MyException):
    pass


class DevicePermissionsException(MyException):
    pass


class FileTypeException(MyException):
    pass


class ReadConfException(MyException):
    pass


class MethodException(MyException):
    pass


class ConfigurationException(MyException):
    pass


class UpdateConfException(MyException):
    pass


class RuntimeException(MyException):
    pass


class UnknownIdentityException(MyException):
    pass


class UnsupportedFile(MyException):
    pass


class SyntaxException(MyException):
    pass


class Parameter(MyException):
    pass


class MatchException(MyException):
    pass

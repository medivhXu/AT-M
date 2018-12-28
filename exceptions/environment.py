#!/usr/bin/env python3


class Environment(Exception):
    def __init__(self, msg):
        super().__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg


class AdbEnvironmentException(Environment):
    pass


class AdbConnectException(Environment):
    pass


class InstrumentsEnvironmentException(Environment):
    pass




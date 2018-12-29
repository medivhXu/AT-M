#!/usr/bin/env python3
import re
from atm.log import LOGGER, logged
from super_classes.commond import Command
from exceptions.environment import AdbEnvironmentException


class Adb(Command):
    def __init__(self):
        super(Adb, self).__init__()

    def _check_adb(self):
        r = self.run_cmd('adb')
        if iter(r):
            for i in r:
                if i.decode() == '-bash: adb: command not found':
                    return False
                else:
                    return True
        else:
            if r.decode() == '-bash: adb: command not found':
                return False
            else:
                return True

    def start_appium(self, udid, add='127.0.0.1', port=4727, bootstrap_port=4728, chrome_port=9519):
        self.run_cmd(
            'appium -a {add} -p {port} -bp {bootstrap_port} --chromedriver-port {chrome_port} -U {udid} --session-override'
            .format(add, port, bootstrap_port, chrome_port, udid))

    def connect(self, ip='127.0.0.1', port=5555):
        if self._check_adb():
            r = self.run_cmd('adb connect {}:{}'.format(ip, port))
            result = [i for i in r[0].decode() if len(re.findall(re.compile('failed.*', re.S), i))]
            if len(result):
                return False
            else:
                return True

    def disconnect(self, ip='127.0.0.1'):
        self.run_cmd('adb disconnect {}'.format(ip))

    def get_devices_version(self):
        r = self.run_cmd('adb shell getprop ro.build.version.release')
        return r or False

    def get_devices_name(self):
        pass

    def get_package_name(self):
        pass


if __name__ == '__main__':
    run = Adb()
    print(run.show_sdk())

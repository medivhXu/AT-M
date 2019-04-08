#!/usr/bin/env python3

from atm.super_classes.commond import Command


class IMobile(Command):
    def __init__(self):
        super(IMobile, self).__init__()

    def start(self):
        pass

    def stop(self):
        pass

    def disconnect(self):
        pass

    def devices():
        """
        Return device dict
        For example:
        {
            "1002038889199992134bad1234112312": "Tony's iPhone"
        }
        """
        udids = [udid.strip() for udid in idevice('_id', '-l').splitlines() if udid.strip()]
        return {udid: idevice('name', '-u', udid).decode('utf-8').strip() for udid in udids}

    def kill_port(self, port):
        raise NotImplementedError

    def check_port(self, port):
        raise NotImplementedError

    def start_appium(self, udid, add='127.0.0.1', port=4727, bootstrap_port=4728, chrome_port=9519):
        pass

    def show_sdk(self):
        raise NotImplementedError

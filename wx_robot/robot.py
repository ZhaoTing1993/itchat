# coding=utf-8

import itchat

from itchat.core import Core

from handler import MonitorHandler, TuringHandler


class WxRobot(object):
    def __init__(self):
        self.handlers = []
        self.default_msg = '听不懂听不懂'
        self.wx = Core()

    def register_handler(self, handler):
        self.handlers.append(handler)

    def dispatch(self):
        @self.wx.msg_register(itchat.content.TEXT)
        def _dispatch(msg):
            print(msg)
            for handler in self.handlers:
                if handler.match(msg):
                    return handler.handle(msg)
            else:
                return self.default_msg

    def run(self):
        self.dispatch()
        self.wx.auto_login(hotReload=True, enableCmdQR=True)
        self.wx.run()


if __name__ == '__main__':
    robot = WxRobot()

    monitor = MonitorHandler()
    turing = TuringHandler()

    robot.register_handler(monitor)
    robot.register_handler(turing)

    robot.run()

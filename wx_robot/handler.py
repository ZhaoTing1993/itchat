from itchat.content import TEXT


class MonitorHandler(object):
    """
    system monitor handler
    """
    HANDLE_MSGS = (TEXT,)

    def __init__(self):
        pass

    def match(self, msg):
        if msg.type in self.HANDLE_MSGS and msg.text.startswith('/m'):
            return True
        return False

    def handle(self, msg):
        return 'monitor'


class XiaoQHandler(object):
    """
    xiaoQ handler
    referer: xiao.douqq.com
    """

    HANDLE_MSGS = (TEXT,)

    def __init__(self):
        pass

    def match(self, msg):
        if msg.type in self.HANDLE_MSGS:
            return True
        return False

    def handle(self, msg):
        return 'xiaoq'

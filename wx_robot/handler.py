# coding=utf-8

from itchat.content import TEXT

from turing import Turing


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


class TuringHandler(object):
    """
    xiaoQ handler
    referer: xiao.douqq.com
    """

    HANDLE_MSGS = (TEXT,)
    turing = Turing()
    userConf = {}

    def __init__(self):
        pass

    def match(self, msg):
        if msg.type in self.HANDLE_MSGS:
            return True
        return False

    def handle(self, msg):
        uid = msg.FromUserName
        if not msg.text or not uid:
            print "no text"
            return
        else:
            print "user:%s, text:%s" % (uid, msg.text.strip())

        if self.userConf.has_key(uid):
            return self.turing.talk(msg.text)

        if msg.text.strip().lower() == 'robot':
            self.userConf.setdefault(uid, 1)
            print "user[%s] registered robot" % uid
            return u'成功开启AI'

        if msg.text.strip().lower() == 'shut up':
            self.userConf.setdefault(uid + "SHUT", 1)
            print "user[%s] shut down robot" % uid
            return u'成功关闭自动回复'

        if not self.userConf.has_key(uid + 'SHUT'):
            return u'【自动回复】主人现在不在\n输入 \'robot\' 唤起AI自动回复\n输入 \'shut up\' 不再提示'
        # return self.turing.talk(msg.text)

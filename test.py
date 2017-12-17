import itchat


@itchat.msg_register(itchat.content.TEXT)
def echo(msg):
    print(msg.text)
    return '[auto-reply]'+msg.text


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run()

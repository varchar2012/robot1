import itchat
import requests

def get_response(_info):
    print(_info)                                       # 从好友发过来的消息
    api_url = 'http://www.tuling123.com/openapi/api'   # 图灵机器人网址
    data = {
        'key': 'ef8c6a6e041b49a0a2397a6f7e9bc0e2',     # 如果这个 apiKey 如不能用，那就注册一次
        'info': _info,                                 # 这是我们从好友接收到的消息 然后转发给图灵机器人
        'userid': 'wechat-robot',                      # 这里你想改什么都可以
    }
    r = requests.post(api_url, data=data).json()       # 把data数据发
    print(r.get('text'))                               # 机器人回复给好友的消息
    return r

@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        if (msg['ActualNickName'] == '孙志超') & ('我是你爸爸' in msg["Text"]) :
            return '爸比亲亲！'
            itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
        elif (msg['ActualNickName'] != '公子今') & ('我是你爸爸' in msg["Text"]):
            return "【IPS僚机--有事请@我】" + "我是你大爷，敢忽悠小爷我？"
            itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])
        elif (msg['ActualNickName'] != '公子今') & ('傻' in msg["Text"]):
            return "【IPS僚机--有事请@我】" + "说话注意点，小心我带着一群小学生挖你家门槛！"
            itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])    
        else :
            return "【IPS僚机--有事请@我】" + get_response(msg["Text"])["text"]
            itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])    
if __name__ == '__main__':
    itchat.auto_login(hotReload=True)                  # hotReload = True, 保持在线，下次运行代码可自动登录
    itchat.run()
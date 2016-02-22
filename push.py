#!/usr/bin/python
# encoding=utf-8

import jpush as JPush
import json


def wrap_app(app_key, master_key):
    return {'app_key': app_key, 'master_key': master_key}


def push(app, title, content, type):

    msg_content = {
        'title': title,
        'description': content,
        'type': type
    }

    jpush = JPush.JPush(app['app_key'], app['master_key'])

    push = jpush.create_push()
    # push.audience = JPush.alias("1547")
    push.audience = JPush.all_
    ios_msg = JPush.ios(alert=content, badge="+1",
                        sound="default", extras=msg_content)

    push.message = JPush.message(msg_content=msg_content)
    push.notification = JPush.notification(ios=ios_msg)
    push.platform = JPush.platform('android', 'ios')
    push.options = {"time_to_live":14400}
    push.send()


# Android测试
android_test = wrap_app('fcec9bf5jas8feg9f1815ef9f', '8c1f23dfo103sdwetoge7bcc')

# IOS测试
ios_test = wrap_app('94d21059osidf966e1a29da', 'e496504oi38f9ahs09qhfa70yq34kj')

# 正式线上，Android和IOS appstroe版本
official = wrap_app('13f39823ojsagea74f4d4d1', '94272sodif9823h9df28ea7')

# IOS企业版
ios_ee = wrap_app('89597203095nasiudcb26', 'bc72247967oiwe0289fasgwl05cf399c')


_title = '金联储'
_content = '猜灯谜，做财迷😍！正月十五来金联储，猜对灯谜送Money💰。让你拿钱拿到手软！'
_type = 'project'

def main():
    # push(ios_ee, _title, _content, _type)
    # push(official, _title, _content, _type)

    ############test##########
    push(android_test, _title, _content, _type)
    # push(official, _title, _content, _type)

if __name__ == '__main__':
    main()

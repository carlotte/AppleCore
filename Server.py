# -*- coding: utf-8 -*-
# filename: Server.py
# auther: John.Titor
# connection: 975534268@qq.com
# This Apple is the orginal one

import web
import Access
import socket
import Recorder.Warning

'''
/Apple用于处理与微信服务器之间的来往信息
/access_token用于服务器内的程序获取访问token
'''
urls = {
    '/Apple','AppleHolder',
    '/access_token','TokenManager',
    '.*','OtherAccessManager',
}

class TokenManager(object):
    def GET(self):
        hostname = socket.getfqdn(socket.gethostname())
        hostaddress = socket.gethostbyname(myname)
        if web.ctx.ip == hostaddress:
            return token_access.get_access_token()
        else:
            Msg = ("TokenAccess from Outside[GET/%s]" % web.ctx.ip)
            Recorder.Warning.Record(Msg, 1)
            return "Apple: Token manager on working, access from inside."
    def POST(self):
        Msg = ("TokenAccess with Post[POST/%s]" % web.ctx.ip)
        Recorder.Warning.Record(Msg, 1)

class OtherAccessManager(object):
    def GET(self):
        Msg = ("Unknown Access[GET/%s]" % web.ctx.ip)
        Recorder.Warning.Record(Msg, 3)
    def POST(self):
        Msg = ("Unknown Access[POST/%s]" % web.ctx.ip)
        Recorder.Warning.Record(Msg, 3)
        
token_access = Access.Access();

if __name__ == '__main__':
    token_access.get_access_token();
    app = web.application(urls, globals(), True)
    app.run()

#!/usr/bin/python3
# -*- coding: utf-8 -*-


import socket
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header


sock = socket.socket()

sock.connect(("www.weather.com.cn", 80))

req = "GET /weather/101200101.shtml HTTP/1.1\r\nConnection close\r\nHost: www.weather.com.cn\r\n\r\n"

sock.send(req.encode())

data = b""
while True:
    tmp = sock.recv(1024)
    if tmp:
        data += tmp
    else:
        break

sock.close()

data = data.decode(errors="ignore")

r = re.findall("value=(.+?)/>", data)

news = r[1]

print(news)


# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "602661651@qq.com"  # 用户名
mail_pass = "dfzoupgsantobdfa"  # 口令

sender = '602661651@qq.com'
receivers = ['602661651@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText(news, 'plain', 'utf-8')
message['From'] = Header("azhe", 'utf-8')
message['To'] = Header("azhe", 'utf-8')

subject = '天气预报'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件", e)
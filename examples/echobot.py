# -*- coding: utf-8 -*-
# original: https://github.com/carpedm20/LINE/blob/master/examples/echobot.py

from line import LineClient, LineGroup, LineContact
from curve.ttypes import TalkException
import os

try:
    line_id = os.environ["LINE_CLIENT_ID"]
    line_pass = os.environ["LINE_CLIENT_PASS"]
except KeyError:
    print "Environment variables not found"
    exit(0)

try:
    client = LineClient(line_id, line_pass, com_name=os.uname()[1], is_mac=False)
    client = LineClient(authToken=client.authToken, com_name=os.uname()[1], is_mac=False)
except TalkException as e:
    print "Login Failed:", e.reason
    exit(0)
else:
    print "Login successful"

while client is not None:
    op_list = []

    try:
        for op in client.longPoll():
            op_list.append(op)

        for op in op_list:
            sender   = op[0]
            receiver = op[1]
            message  = op[2]

            msg = message.text
            sender.sendMessage("[%s] %s" % (sender.name, msg)) #send message back to sender
    except Exception as e:
        print e

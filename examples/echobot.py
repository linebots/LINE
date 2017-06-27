# original: https://github.com/carpedm20/LINE/blob/master/examples/echobot.py

from line import LineClient, LineGroup, LineContact
import os

line_id = os.environ["LINE_CLIENT_ID"]
line_pass = os.environ["LINE_CLIENT_PASS"]

try:
   #client = LineClient("ID", "PASSWORD")
   client = LineClient(line_id, line_pass, com_name="Display Name")
   #print client.authToken #print authToken before error and use this login again
   #client = LineClient(authToken="AUTHTOKEN")
   client = LineClient(authToken=client.authToken)
except:
   print "Login Failed"
   exit()

while True:
   op_list = []

   for op in client.longPoll():
      op_list.append(op)

   for op in op_list:
      sender   = op[0]
      receiver = op[1]
      message  = op[2]

      msg = message.text
      sender.sendMessage("[%s] %s" % (sender.name, msg)) #send message back to sender

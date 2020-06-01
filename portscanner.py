import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Target Invalid")

print('-'*50)
print("Scanning Target")
print("Time started:"+str(datetime.now()))
print('-'*50)

try:
    for port in range(0,65535):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print ("Exiting Program")
    sys.exit()

except socket.gaierror:
    print("Could not resolve host")
    sys.exit()

except socket.error:
    print("Could not connect to server")
    sys.exit()

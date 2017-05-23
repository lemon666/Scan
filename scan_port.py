# -*- coding: utf-8 -*-
import socket
import threading
def portscan(port):
		s=socket.socket();
		#s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.settimeout(1)
		try:
			s.connect(('119.75.218.70',port))
			print str(port) + " open"
		except:
			pass
threads=[]
for i in range(10000):
	threads.append(threading.Thread(target=portscan,args=(i,)))
for t in threads:
	t.start()
for k in threads:
	k.join()
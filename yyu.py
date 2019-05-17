import serial
import time
import thread

port = serial.Serial("/dev/tty8",baudrate=115200,timeout=0.5)

print port.portstr

#def recv_func(sec):
	
#global port
print 'send'
port.write(chr(0x06).encode("utf-8"))
port.write(chr(0x06))
port.write('hello') 
#port.xonxoff=True
print 'RECV'
print port.stopbits
print port.xonxoff
print 'is hw flow control?'
print port.rtscts
print port.dsrdtr
#not success
#learn git
i =0	
while True:
	readbuff=port.read(10)
	print readbuff
	i=i+1
	print i
	
	time.sleep(2)



'''
if __name__ == '__main__':
    thread.start_new_thread(recv_func(2))'''



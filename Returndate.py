# -.- coding:utf-8 -.-
import socket,time,struct

PORT = 8080
HOST = 'Localhost'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

def returndate(date):
    changedtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(date))
    return changedtime

def ts2time(date):
    data = time.localtime(date)
    print data
    year = data[0]
    month = data[1]
    day = data[2]
    hour = data[3]
    minute = data[4]
    second = data[5]
    s = bytearray(7)
    s[0] = year/256
    s[1] = year%256
    s[2] = month
    s[3] = day
    s[4] = hour
    s[5] = minute
    s[6] = second
    ss = ''  #输出测试用
    for i in range(0,7):
        ss =ss +' '+ '%02x'%(s[i])
    str = struct.pack('HBBBBB',year,month,day,hour,minute,second)
    return str

while 1:
    clientsock,clientaddr = s.accept()
    requestdata = clientsock.recv(1024)
    
    #服务器时间戳
    nowtime_X = time.time()
    result = ts2time(nowtime_X)
    result = struct.unpack('HBBBBB',result)
    print result
    clientsock.send(result)
    clientsock.close()

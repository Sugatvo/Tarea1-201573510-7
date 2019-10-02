import socket
from _thread import *
import threading
import struct
import sys

print_lock = threading.Lock()
def threaded(c, multicast_group, opcion):
    if(opcion == "estado"):
        while True:
            data, address = c.recvfrom(1024)
            respuesta = "Datanode 3: Activo "
            c.sendto(respuesta.encode('ascii'), address)

    else:
        while True:
            data = c.recv(1024)
            write_data = data.decode() + "\n"
            file = open("data.txt","a")
            file.write(write_data)
            file.close()
            print("Mensaje guardado!!")

            respuesta = "registro correcto de datos"
            c.send(respuesta.encode('ascii'))
            print_lock.release()
            break
    c.close()



def Main():
    multicast_group = '224.10.10.10'
    server_address = ('', 10000)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(server_address)

    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(
        socket.IPPROTO_IP,
        socket.IP_ADD_MEMBERSHIP,
        mreq)

    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4.bind(("0.0.0.0", 5003))
    s4.listen(5)

    start_new_thread(threaded, (sock, multicast_group, "estado"))

    while True:
        c, addr = s4.accept()
        print_lock.acquire()
        start_new_thread(threaded, (c, multicast_group, "cliente"))
    s.close()

if __name__ == '__main__':
    Main()

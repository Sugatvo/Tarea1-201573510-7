import socket
from _thread import *
import threading
import time

print_lock = threading.Lock()
def threaded(c):
    while True:
        data = c.recv(1024)
        ip, port = c.getpeername()

        write_data = "IP: " + str(ip) + " - Mensaje: " + data.decode()
        print(write_data)
        localtime = time.asctime( time.localtime(time.time()) )
        write_data = localtime + " - "  + write_data + "\n"

        file = open("log.txt","a")
        file.write(write_data)
        file.close()

        respuesta = "Se recibio correctamente la peticion"
        c.send(respuesta.encode('ascii'))

    print_lock.release()
    c.close()


def Main():
    host = '0.0.0.0'
    port = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("Server creado en puerto: ", port)
    s.listen(5)
    while True:
        c, addr = s.accept()
        print_lock.acquire()
        print('Conectado a:', addr[0], ' -', addr[1])
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()

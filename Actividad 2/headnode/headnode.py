import socket
from _thread import *
import threading
import struct
import time
import random

print_lock = threading.Lock()
def threaded(c, multicast_group, opcion, destinos):
    if(opcion == "estado"):
        while True:
            consulta = "Se encuentra operativo?"
            sent = c.sendto(consulta.encode('ascii'), multicast_group)

            write_data = "Status - "
            try:
                data1, server1 = c.recvfrom(1024)
                write_data += data1.decode()
                data2, server2 = c.recvfrom(1024)
                write_data += " - " + data2.decode()
                data3, server3 = c.recvfrom(1024)
                write_data += " - " + data3.decode()
            except socket.timeout:
                None

            if("Datanode 1: Activo" not in write_data):
                write_data = "Datanode 1: Inactivo"
            if("Datanode 2: Activo" not in write_data):
                write_data = "Datanode 2: Inactivo"
            if("Datanode 3: Activo" not in write_data):
                write_data = "Datanode 3: Inactivo"

            print(write_data)
            localtime = time.asctime( time.localtime(time.time()) )
            write_data = localtime + " : "  + write_data + "\n"

            file = open("hearbeat_server.txt","a")
            file.write(write_data)
            file.close()

            time.sleep(5)
    else:
        while True:
            data = c.recv(1024)

            random.seed()
            n_random = random.randint(0,2)

            print("Enviando mensaje a Datanode " + str(n_random+1))
            s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s1.connect(destinos[n_random])

            s1.send(data)
            data1 = s1.recv(1024)

            write_data = "Datanode " + str(n_random + 1) + " - Mensaje: " + data.decode() + "\n"
            file = open("registro_server.txt","a")
            file.write(write_data)
            file.close()

            mensaje_cliente = data.decode() + ": Guardado en datanode " + str(n_random + 1) + "\n"
            c.send(mensaje_cliente.encode('ascii'))

            s1.close()


    print_lock.release()
    c.close()


def Main():
    multicast_group = ('224.10.10.10', 10000)
    server_address = ('', 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(server_address)
    print("¡Server creado!")

    s.settimeout(0.5)
    ttl = struct.pack('b', 1)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4.bind(("0.0.0.0", 5004))
    s4.listen(5)

    destinos = [("datanode_1", 5001), ("datanode_2", 5002), ("datanode_3", 5003)]

    start_new_thread(threaded, (s, multicast_group, "estado", destinos))

    while True:
        c, addr = s4.accept()
        print_lock.acquire()
        print('Conectado con:', addr[0], ' -', addr[1])
        start_new_thread(threaded, (c, multicast_group, "cliente", destinos))
    s.close()
    s4.close()


if __name__ == '__main__':
    Main()

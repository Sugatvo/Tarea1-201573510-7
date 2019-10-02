import socket
import time

def Main():
    host = "headnode"
    port = 5004
    time.sleep(10) # Enviar mensajes cada 10 segundos

    tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpClient.connect((host, port))

    i = 1
    while True:
        # Manda el mensaje de solicitud al servidor
        mensaje = "Mensaje " + str(i)
        print("Enviando mensaje...")
        tcpClient.send(mensaje.encode('ascii'))

        # Recibe la confirmacion
        data = tcpClient.recv(1024)

        file = open("registro_cliente.txt","a")
        file.write(data.decode())
        file.close()
        i += 1
        time.sleep(10) # Enviar mensajes cada 10 segundos

    print("¡Conexion finalizada!")
    tcpClient.close()

if __name__ == '__main__':
    Main()

import socket
import time

def Main():
    host = "servidor"
    port = 5000
    BUFFER_SIZE = 2000

    tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpClient.connect((host, port))
    print("Conexion realizada!!!")

    while True:
        # Manda el mensaje de solicitud al servidor
        mensaje = "Hola querido servidor"
        print(mensaje)
        tcpClient.send(mensaje.encode('ascii'))

        # Recive la confirmacion
        data = tcpClient.recv(BUFFER_SIZE)
        write_data = data.decode() + "\n"

        file = open("respuestas.txt","a")
        file.write(write_data)
        file.close()
        time.sleep(5) # Enviar mensajes cada 10 segundos

    print("¡Conexion finalizada!")
    tcpClient.close()


if __name__ == '__main__':
    Main()

# Consideraciones

1. El cliente envía mensajes cada 10 segundos al headnode.
2. El headnode envía el mensaje a un datanode elegido aleatoriamente.
3. Los Path de "data.txt": Se encuentran en las carpetas de los datanode_i. Con i = [1,2,3].
4. Path de "hearbeat_server.txt" y "registro_server.txt": La carpeta "headnode" de este mismo directorio.
5. Path de "registro_cliente.txt": La carpeta "cliente" de este mismo directorio.
6. Los archivos de texto se generan automáticamente.

import socket
mi_socket=socket.socket()
mi_socket.bind(('localhost',8000))
mi_socket.listen(5)

while True:
    conexion,addr=mi_socket.accept()
    print('nueva conexión')
    print(addr)
    
    conexion.send("soy el servidor".encode())
    
    conexion.close()

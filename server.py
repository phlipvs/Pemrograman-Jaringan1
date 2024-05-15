import socket

# Inisialisasi socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind ke alamat dan port tertentu
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Mendengarkan koneksi masuk
server_socket.listen(1)

print("Server berjalan di", server_address)

while True:
    # Menerima koneksi
    client_socket, client_address = server_socket.accept()
    
    print("Terhubung dengan", client_address)
    
    try:
        while True:
            # Menerima data dari klien
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Menghitung jumlah karakter dalam pesan
            message_length = len(data)
            response = "Jumlah karakter: {}".format(message_length)
            
            # Mengirimkan balasan ke klien
            client_socket.sendall(response.encode())
    finally:
        # Menutup koneksi
        client_socket.close()

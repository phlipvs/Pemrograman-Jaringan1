import socket

# Inisialisasi socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Membuat koneksi ke server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Meminta input dari pengguna
    message = input("Masukkan pesan: ")
    
    # Mengirimkan pesan ke server
    client_socket.sendall(message.encode())
    
    # Menerima balasan dari server
    response = client_socket.recv(1024)
    print("Balasan dari server:", response.decode())
finally:
    # Menutup koneksi
    client_socket.close()

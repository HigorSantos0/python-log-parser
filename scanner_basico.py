import socket

ip_alvo = "127.0.0.1"
porta_teste = 80

for porta_teste in range(1, 1025):

    meu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    meu_socket.settimeout(1)

    print(f"Tentando conectar no IP {ip_alvo} na porta {porta_teste}...")

    resultado = meu_socket.connect_ex((ip_alvo, porta_teste))

    if resultado == 0:
        print(f"[+] Porta {porta_teste} está ABERTA!")

    meu_socket.close()

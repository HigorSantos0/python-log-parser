import socket
import concurrent.futures

ip_alvo = input("Digite o IP ou site que deseja escanear: ")

def testar_porta(porta):
    meu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meu_socket.settimeout(1)
    
    resultado = meu_socket.connect_ex((ip_alvo, porta))
    
    if resultado == 0:
        print(f"[+] Porta {porta} está ABERTA!")
        
    meu_socket.close()


print(f"Iniciando scan no IP {ip_alvo}...")

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    
    for porta in range(1, 1025):
        executor.submit(testar_porta, porta)

print("Scan finalizado!")
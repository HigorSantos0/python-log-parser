import requests
import csv
import requests
import os


arquivo_log = "auth.log"
print("Iniciando análise de segurança e geolocalização...\n")

contagem_ips = {}

# ==========================================
# FASE 1: LER O LOG E CONTAR (Sem usar a API)
# ==========================================
with open(arquivo_log, "r") as arquivo:
    for linha in arquivo:
        if "Failed" in linha:
            parte_final = linha.split("from ")[1]
            ip_atacante = parte_final.split(" ")[0]
            
            # Se o IP já está no dicionário, adicio +1 na conta.
            if ip_atacante in contagem_ips:
                contagem_ips[ip_atacante] += 1
            # Se for a primeira vez que vemos o IP, a conta começa em 1.
            else:
                contagem_ips[ip_atacante] = 1

# ==========================================
# FASE 2: INVESTIGAR E EXPORTAR (ETL + FIREWALL)
# ==========================================
limite_tolerancia = 3 

pasta_saida = "relatorios"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

caminho_csv = f"{pasta_saida}/alertas_seguranca.csv"
caminho_blacklist = f"{pasta_saida}/blacklist.txt"

#Lemos a blacklist atual para garantir dados únicos
ips_ja_bloqueados = set()
if os.path.exists(caminho_blacklist):
    with open(caminho_blacklist, "r", encoding="utf-8") as arquivo_txt:
        for linha in arquivo_txt:
            ips_ja_bloqueados.add(linha.strip())

# Adicionando novos dados
with open(caminho_csv, "a", newline="", encoding="utf-8") as arquivo_csv:
    with open(caminho_blacklist, "a", encoding="utf-8") as arquivo_txt:
        escritor = csv.writer(arquivo_csv)
        
        # Só escreve se estiver vazio
        if arquivo_csv.tell() == 0:
            escritor.writerow(["IP", "Tentativas", "Cidade", "Pais"])

        for ip, quantidade in contagem_ips.items():
            if quantidade >= limite_tolerancia:
                
                # VERIFICAÇÃO DE DUPLICIDADE
                if ip in ips_ja_bloqueados:
                    print(f"✅ O IP {ip} já está na blacklist. Ignorando...")
                    continue # Pula toda a lógica abaixo e vai para o próximo IP

                print(f"⚠️ ATENÇÃO: O IP {ip} tentou invadir {quantidade} vezes. Consultando origem...")
                
                try:
                    url_api = f"http://ip-api.com/json/{ip}"
                    resposta = requests.get(url_api)
                    dados_localizacao = resposta.json()
                    
                    if dados_localizacao.get("status") == "success":
                        pais = dados_localizacao.get("country")
                        cidade = dados_localizacao.get("city")
                        print(f"🔥 NOVO BLOQUEIO GERADO: IP {ip} | Origem: {cidade}, {pais}\n")
                        escritor.writerow([ip, quantidade, cidade, pais])
                        
                    else:
                        print(f"🔥 NOVO BLOQUEIO GERADO: IP {ip} | Origem: Desconhecida\n")
                        escritor.writerow([ip, quantidade, "Desconhecida", "Desconhecida"])
                    
                    arquivo_txt.write(ip + "\n")
                    
                    # atualizado em memória
                    ips_ja_bloqueados.add(ip)
                        
                except Exception as e:
                    print(f"🔥 ERRO DE CONEXÃO AO INVESTIGAR IP {ip}\n")

print("Análise, Exportação e Geração de Blacklist concluídas!")
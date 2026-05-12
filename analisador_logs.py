arquivo_log = "auth.log"
print("Iniciando análise de segurança nos logs...\n")

with open(arquivo_log, "r") as arquivo:

    for linha in arquivo:
        if "Failed" in linha:
            print(f"[ALERTA] Invasão detectada: {linha.strip()}")
        

print("\nAnálise concluída!")
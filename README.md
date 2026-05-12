# 🛡️ SecOps Log Analyzer & IP Extractor

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Blue_Team-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

> Um script ágil focado em operações de **Blue Team / Defesa**, desenvolvido para atuar como um processo de ETL (Extração, Transformação e Carregamento) em logs de servidores Linux.

---

## 🎯 Visão Geral
Servidores expostos à internet sofrem constantes ataques de força bruta, especialmente na porta 22 (SSH). Este projeto automatiza a primeira linha de defesa: a análise de logs. 

O script varre arquivos de registro do sistema (como o `auth.log`), identifica padrões de autenticação falha, filtra o "ruído" (logins legítimos) e extrai **apenas o endereço IP do atacante**, gerando inteligência acionável para bloqueio em Firewalls ou Security Groups.

## ✨ Funcionalidades
* **Leitura Eficiente:** Processa o arquivo de log linha por linha.
* **Filtragem de Ameaças:** Isola apenas as tentativas de invasão (`Failed password`).
* **Extração de Dados (Parsing):** Corta e limpa a string do log para isolar o IP de origem do ataque usando técnicas de manipulação de texto.

---

## 🚀 Como Executar

### Pré-requisitos
* Python 3 instalado no sistema.
* Um arquivo de log (ex: `auth.log`) no mesmo diretório do script.

### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)

2. Acesse a pasta do projeto:
    ```bash
    cd SEU_REPOSITORIO

3. Execute o analisador:
    ```bash
    python analisador_logs.py


📊 Exemplo de Saída
Log Original (Sujo):
    ```Plaintext
    May 11 10:05:05 servidor sshd[4521]: Failed password for root from 203.0.113.42 port 33215

Resultado do Script (Limpo e Acionável):

Iniciando análise de segurança nos logs...

🔥 ALERTA CRÍTICO: Tentativa de invasão vinda do IP: 203.0.113.42
🔥 ALERTA CRÍTICO: Tentativa de invasão vinda do IP: 8.8.4.4

Análise concluída!




Projeto desenvolvido para fins de estudo em Segurança da Informação e Automação de Infraestrutura.
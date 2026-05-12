# 🛡️ SecOps Log Analyzer & Threat Intelligence Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Blue_Team-blue?style=for-the-badge)
![Data Engineering](https://img.shields.io/badge/ETL-Pipeline-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

> Ferramenta automatizada para operações de **Blue Team**, desenvolvida em Python. Atua como um processo completo de ETL para logs de servidores, transformando registros brutos de ataques em inteligência acionável e regras de Firewall.

---

## 🎯 Visão Geral
Servidores expostos à internet sofrem constantes ataques de força bruta, especialmente na porta 22 (SSH). Este projeto automatiza a primeira linha de defesa lendo logs do sistema, extraindo os IPs dos atacantes e enriquecendo esses dados via APIs de **Threat Intelligence** (Geolocalização).

O script gera relatórios gerenciais estruturados e cria automaticamente uma **Lista de Bloqueio (Blacklist)** para uso imediato em regras de Firewall ou Security Groups.

## ✨ Funcionalidades
* **Extração Eficiente:** Faz o parsing de logs do Linux isolando tentativas de invasão (`Failed password`).
* **Enriquecimento de Dados:** Integração com a **IP-API** para rastrear País e Cidade de origem do ataque.
* **Otimização de Performance:** Uso de Dicionários e Conjuntos (`sets`) para evitar duplicidade de consultas e sobrecarga da API.
* **Pipeline ETL (Load):** Exporta os dados agregados para `.csv` e gera um arquivo `.txt` contendo a Blacklist pronta para deploy.

---

## 🚀 Como Executar

### Pré-requisitos
* Python 3 instalado no sistema.
* Instalar a biblioteca de requisições web:
  ```bash
  pip install requests


  Passo a passo: 

  git clone [https://github.com/HigorSantos0/python-log-parser.git](https://github.com/HigorSantos0/python-log-parser.git)


  Acesse a pasta do projeto:

  cd SEU_REPOSITORIO

  Execute o analisador

  python analisador_logs.py



  ---

## 📊 Artefatos Gerados (Saída)

Após a execução, o script cria automaticamente a pasta `relatorios/` contendo:

**1. Relatório Gerencial (`alertas_seguranca.csv`):**
| IP | Tentativas | Cidade | Pais |
| :--- | :--- | :--- | :--- |
| 203.0.113.42 | 4 | New York | United States |

**2. Regra de Firewall (`blacklist.txt`):**
```text
203.0.113.42
8.8.4.4
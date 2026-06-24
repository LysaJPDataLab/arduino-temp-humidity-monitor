# Pipeline IoT: Monitoramento de Temperatura e Umidade com Arduino e Google Cloud

## 📌 Visão Geral
Este projeto consiste no desenvolvimento de um sistema de aquisição, processamento e visualização de dados climáticos locais. A arquitetura engloba a coleta de dados de temperatura e umidade via hardware (Arduino), a transmissão serial para um ambiente local, e o envio automatizado para a nuvem (Google Sheets) via script Python. A visualização final é realizada através de um dashboard interativo.

## 🏗️ Arquitetura do Projeto
O fluxo de dados foi estruturado nas seguintes etapas:
1. **Coleta (Hardware):** Um Arduino Uno e um sensor DHT11 realizam as leituras físicas do ambiente a cada 30 segundos.
2. **Interface Serial:** Os dados brutos são transmitidos via porta serial (USB) para um computador local.
3. **Ingestão e Processamento (Python):** Um script em Python, utilizando a biblioteca `pyserial`, lê os dados da porta COM, realiza a limpeza dos caracteres e formata as variáveis.
4. **Armazenamento em Nuvem:** Utilizando `gspread` e autenticação via Google Cloud Service Account, o script faz o *append* contínuo dos dados em uma planilha do Google Sheets.
5. **Visualização:** Os dados armazenados alimentam um dashboard criado no Looker Studio, disponibilizado publicamente em um site produzido no Canva.

## 🛠️ Tecnologias e Ferramentas

| Categoria | Tecnologias |
| :--- | :--- |
| **Hardware** | Arduino Uno, Módulo Sensor DHT11 |
| **Linguagens** | C++ (Arduino IDE), Python |
| **Bibliotecas Python** | `pyserial`, `gspread`, `oauth2client` |
| **Cloud** | Google Cloud Platform (IAM/Service Accounts) |
| **Armazenamento de dados** | Google Sheets |
| **Visualização de dados** | Looker Studio |
| **Site** | Canva |

## 🚀 Como Executar o Projeto

### Pré-requisitos
* **[Arduino IDE](https://www.arduino.cc/en/software)** instalada e placa Arduino Uno configurada.
* **[Python 3.x](https://www.python.org/downloads/)** instalado no seu sistema.
* Conta no **[Google Cloud Console](https://console.cloud.google.com/)** com as APIs do Google Drive e Google Sheets ativadas, e uma Service Account criada.

### Passo a Passo
1. **Montagem do Circuito:** Conecte o pino de dados do sensor DHT11 ao pino digital 3 do Arduino.
2. **Upload do Código:** Abra o arquivo `arduino/sketch_monitoramento.ino` na Arduino IDE, instale a biblioteca `DHT sensor library` e faça o upload para a placa.
3. **Configuração do Ambiente Python:**
   ```bash
   cd python
   pip install -r requirements.txt

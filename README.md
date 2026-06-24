# ⛅Pipeline IoT: Monitoramento de Temperatura e Umidade com Arduino e Google Cloud

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Hardware](https://img.shields.io/badge/Hardware-Arduino_Uno-00979D?logo=arduino&logoColor=white)
![Linguagem](https://img.shields.io/badge/Script-Python-3776AB?logo=python&logoColor=white)
![Cloud](https://img.shields.io/badge/Cloud-Google_Cloud-4285F4?logo=googlecloud&logoColor=white)
![Database](https://img.shields.io/badge/Database-Google_Sheets-34A853?logo=googlesheets&logoColor=white)
![Dashboard](https://img.shields.io/badge/Dashboard-Looker_Studio-4285F4?logo=looker&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-Canva-00C4CC?logo=canva&logoColor=white)

## 📌 Visão Geral
Este projeto consiste no desenvolvimento de um sistema de aquisição, processamento e visualização de dados climáticos locais. A arquitetura engloba a coleta de dados de temperatura e umidade via hardware (Arduino), a transmissão serial para um ambiente local, e o envio automatizado para a nuvem (Google Sheets) via script Python. A visualização final é realizada através de um dashboard interativo.

   ![Esquema do Circuito](assets/Dashboard_DataTemp.PNG)
   
## 🏗️ Arquitetura do Projeto
O fluxo de dados foi estruturado nas seguintes etapas:

1. **Coleta (Hardware):** Um Arduino Uno e um sensor DHT11 realizam as leituras físicas do ambiente a cada 30 segundos.
2. **Interface Serial:** Os dados brutos são transmitidos via porta serial (USB) para um computador local.
3. **Ingestão e Processamento (Python):** Um script em Python, utilizando a biblioteca `pyserial`, lê os dados da porta COM, realiza a limpeza dos caracteres e formata as variáveis.
4. **Armazenamento em Nuvem:** Utilizando `gspread` e autenticação via Google Cloud Service Account, o script faz o *append* contínuo dos dados em uma planilha do Google Sheets.
5. **Visualização:** Os dados armazenados alimentam um dashboard criado no Looker Studio, disponibilizado publicamente em um site produzido no Canva.

![Diagrama de Overview do Projeto](assets/diagrama_esquematico_projeto.PNG)

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

1. **Montagem do Circuito:** Conecte o pino de dados (DATA) do sensor DHT11 ao pino digital 3 do Arduino. Em seguida, alimente o sensor conectando o seu pino VCC ao pino 5V do Arduino, e o pino GND ao GND do Arduino. 
*Nota:* A alimentação e a comunicação do Arduino devem ser feitas obrigatoriamente via cabo USB conectado ao computador, pois neste projeto o script Python precisa ler os dados da porta serial em tempo real para enviá-los à nuvem.
   
   ![Esquema do Circuito](assets/esquema_monitoramento_de_temperatura.PNG)

2. **Upload do Código:** Abra o arquivo `arduino/sketch_monitoramento.ino` na Arduino IDE, instale a biblioteca `DHT sensor library` e faça o upload para a placa.

   ![Esquema do Circuito](assets/arduino_IDE_sketch.PNG)

3. **Configuração do Ambiente Python:**
   ```bash
   cd python
   pip install -r requirements.txt

## 📊 Visualização e Dashboard

Os dados em tempo real e o histórico de monitoramento podem ser visualizados na nossa interface pública.

🌐 **Acesse o site do projeto:** [DataTemp - Monitoramento Climático](https://datatemptucano.my.canva.site/)

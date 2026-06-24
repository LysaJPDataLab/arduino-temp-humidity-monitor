import serial 
import gspread 
from oauth2client.service_account import ServiceAccountCredentials 
import time 

# =====================================================================
# CONFIGURAÇÕES DE AMBIENTE (Edite conforme necessário)
# =====================================================================
ARQUIVO_CREDENCIAIS = "credentials.json"
NOME_PLANILHA = "Dados_DataTemp"
PORTA_SERIAL = 'COM4'                     # Ex: 'COM4' (Windows) ou '/dev/ttyUSB0' (Linux)
BAUD_RATE = 9600
# =====================================================================

# Configuração do Google Sheets 
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"] 
creds = ServiceAccountCredentials.from_json_keyfile_name(ARQUIVO_CREDENCIAIS, scope) 
client = gspread.authorize(creds) 
sheet = client.open(NOME_PLANILHA).sheet1 

# Configuração do Serial 
ser = serial.Serial(PORTA_SERIAL, BAUD_RATE) 
time.sleep(2)  # Aguarda a conexão estabilizar 

while True: 
    if ser.in_waiting > 0: 
        line = ser.readline().decode('utf-8').strip() 
        data = line.split() 
        
        if len(data) == 4: 
            temperature = float(data[1].replace("℃", ""))  # Remove o símbolo antes de converter 
            humidity = float(data[3].replace("%", ""))     # Remove o símbolo de % 
            
            # Envia para a nuvem
            sheet.append_row([time.strftime('%Y-%m-%d %H:%M:%S'), temperature, humidity])

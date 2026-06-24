import serial 
import gspread 
from oauth2client.service_account import ServiceAccountCredentials 
import time 

# Configuração do Google Sheets 
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"] 
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope) 
client = gspread.authorize(creds) 
sheet = client.open("Dados_DataTemp").sheet1 

# Configuração do Serial 
ser = serial.Serial('COM4', 9600)  # Definição da porta 
time.sleep(2)  # Aguarda a conexão estabilizar 

while True: 
    if ser.in_waiting > 0: 
        line = ser.readline().decode('utf-8').strip() 
        data = line.split() 
        
        if len(data) == 4: 
            temperature = float(data[1].replace("℃", ""))  # Remove o símbolo "℃" antes de converter 
            humidity = float(data[3].replace("%", ""))  # Se houver símbolo "%" na umidade, faça o mesmo 
            sheet.append_row([time.strftime('%Y-%m-%d %H:%M:%S'), temperature, humidity])
// Banco de dados de temperatura e umidade 
#include <DHT.h>        // inclusão da biblioteca DHT lib   

#define DHTPIN 3        // Pino ao qual o sensor está conectado
#define DHTTYPE DHT11   // Tipo de sensor

DHT dht(DHTPIN, DHTTYPE);  // Criação objeto DHT

void setup() {
  Serial.begin(9600);   //Inicia comunicação serial
  delay(6000);          // Aguarda o sensor 
  Serial.println("Leitura de Temperatura e Umidade"); 
  dht.begin();          // Inicializa o sensor
}
  // Leitura da temperatura e umidade
void loop() {
  delay(2000); // Aguarda 2 segundos entre as leituras

  float h = dht.readHumidity();    // Leitura da umidade 
  float t = dht.readTemperature(); // Leitura da temperatura em Celsius

  // Verifica se houve erro na leitura
  if (isnan(h) || isnan(t)) {
    Serial.println("Erro ao ler o sensor DHT11!");
    return;
  }

  Serial.print("Temperatura: ");
  Serial.print(t);
  Serial.print("℃\t");
  Serial.print("Umidade: ");
  Serial.println(h);
  Serial.print("%");
  delay(30000);                   //Aguarda 30 segundos para enviar novamente
}
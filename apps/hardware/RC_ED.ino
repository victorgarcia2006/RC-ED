#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "S24 FE de García Calvillo";
const char* password = "08Mayo_2006";
const char* apiUrl = "https://rc-ed-production.up.railway.app/api/monitoreo/experiment-data/";

const int pinCapacitor = 34;     // Pin analógico donde se mide el voltaje del capacitor
bool midiendo = false;           // Indica si la medición está activa
unsigned long tiempoInicio = 0;  // Guarda el momento en que se presiona el botón

struct Dato {
  unsigned long t;
  float v;
};

Dato datos[100];   // Ajusta según la duración de la medición
int indice = 0;

void setup() {
  Serial.begin(115200);
  analogSetAttenuation(ADC_11db);  // Rango de 0 a ~3.6 V
  delay(1000);
  Serial.println("Conectando al WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi conectado!");
}

void loop() {
  // Detecta si el botón fue presionado (estado LOW porque usamos INPUT_PULLUP)
  int raw = analogRead(pinCapacitor);
  float voltage = (raw / 4095.0) * 3.04;  // Conversión directa
  if (voltage >= 2.99 && !midiendo) {
    midiendo = true;
    tiempoInicio = millis();  // Marca el inicio de la medición
    Serial.println("Medición iniciada...\n");
  }

  if (midiendo) {
    unsigned long tiempoActual = millis() - tiempoInicio;  // Tiempo transcurrido desde que empezó la medición
    if (indice < 500) {
      datos[indice++] = {tiempoActual, voltage};
    }

    Serial.print("Tiempo: ");
    Serial.print(tiempoActual);
    Serial.print(" ms\tVoltaje: ");
    Serial.print(voltage, 3);
    Serial.println(" V");

    delay(30);

    if(voltage == 0){
      midiendo = false;
      enviarDatos();
    }
  }
}

void enviarDatos() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(apiUrl);
    http.addHeader("Content-Type", "application/json");

    // Construimos JSON
    DynamicJsonDocument doc(8192);
    JsonArray arr = doc.to<JsonArray>();

    for (int i = 0; i < indice; i++) {
      JsonObject obj = arr.createNestedObject();
      obj["t"] = datos[i].t;
      obj["v"] = datos[i].v;
    }

    String jsonString;
    serializeJson(doc, jsonString);

    Serial.println("JSON generado:");
    Serial.println(jsonString);

    int httpResponseCode = http.POST(jsonString);

    if (httpResponseCode > 0) {
      Serial.print("Datos enviados correctamente. Código: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.print("Error al enviar los datos: ");
      Serial.println(http.errorToString(httpResponseCode).c_str());
    }

    http.end();
  } else {
    Serial.println("Error: WiFi desconectado, no se pudo enviar la información.");
  }
}

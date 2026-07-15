#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

// ---------------- WIFI ----------------
const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

// ---------------- MQTT ----------------
const char* mqtt_server = "broker.hivemq.com";

WiFiClient espClient;
PubSubClient client(espClient);

// ---------------- DHT ----------------
#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup_wifi() {
    delay(10);

    Serial.println();
    Serial.print("Connecting to WiFi");

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println();
    Serial.println("WiFi connected");
}

void reconnect() {
    while (!client.connected()) {

        Serial.print("Connecting to MQTT...");

        if (client.connect("ESP32Client")) {
            Serial.println("connected");
        } else {
            Serial.print("failed, rc=");
            Serial.print(client.state());
            delay(2000);
        }
    }
}

void setup() {

    Serial.begin(115200);

    dht.begin();

    setup_wifi();

    client.setServer(mqtt_server, 1883);
}

void loop() {

    if (!client.connected()) {
        reconnect();
    }

    client.loop();

    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();

    if (isnan(temperature) || isnan(humidity)) {
        Serial.println("Failed to read from DHT sensor!");
        delay(2000);
        return;
    }

    char tempString[8];
    dtostrf(temperature, 1, 2, tempString);

    char humString[8];
    dtostrf(humidity, 1, 2, humString);

    client.publish("iiitv/temperature", tempString);
    client.publish("iiitv/humidity", humString);

    Serial.print("Temperature: ");
    Serial.println(tempString);

    Serial.print("Humidity: ");
    Serial.println(humString);

    Serial.println("-------------------");

    delay(2000);
}
#include <esp_now.h>
#include <WiFi.h>
#include "../sensors_data.h"

esp_now_peer_info_t peer;

sensors_data data;

// TODO: coloque um mac válido para o receptor
uint8_t slave_addr[] = { 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };

void setup() {
	Serial.begin(115200);

	WiFi.mode(WIFI_STA);
	Serial.println(WiFi.macAddress());

	if(esp_now_init() != ESP_OK) {
		ESP.restart();
	}

	peer.channel = 1;
	peer.encrypt = 0;

	memcpy(peer.peer_addr, slave_addr, 6);
	esp_now_add_peer(&peer);
}

void loop() {
	data.vel = 123;
	data.rpm = 321;
	data.comb = 213;

	if (esp_now_send(slave_addr, (uint8_t *) &data,
		sizeof(sensors_data)) != ESP_OK) {

		Serial.println("Erro!");
	} else {
		Serial.println("Sucesso!");
	}

	delay(64);
}

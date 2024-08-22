#include <esp_now.h>
#include <WiFi.h>
#include "../sensors_data.h"

sensors_data recv_data;

void data_recv(const esp_now_recv_info *sender,
	const unsigned char *data, int len) {

	memcpy(&recv_data, data, len);

	Serial.printf("%.2f\n", recv_data.vel);
	Serial.printf("%d\n", recv_data.rpm);
	Serial.printf("%d\n", recv_data.comb);

	Serial.printf("[%d]\n", len);
}

void setup() {
	Serial.begin(115200);

	WiFi.mode(WIFI_STA);

	if(esp_now_init() != ESP_OK) {
		Serial.println("erro ao iniciar o espnow!");
		ESP.restart();
	}

	esp_now_register_recv_cb(data_recv);
}

void loop() {
}

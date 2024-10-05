#include <ArduinoJson.h>

JsonDocument data_json;

void setup() {
	Serial.begin(9600);
	while (!Serial) {
		continue;
	}

	randomSeed(analogRead(0));
}

void loop() {
	data_json["velo"] = random(0, 50);
	data_json["temp"] = random(30, 300);

	serializeJson(data_json, Serial);
	Serial.println();

	delay(100);
}

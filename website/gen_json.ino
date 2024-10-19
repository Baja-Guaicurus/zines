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
  data_json["rpm"] = random(0, 3e3);
  data_json["comb"] = random(0, 100);
  data_json["temp_cvt"] = random(30, 300);
	data_json["velo"] = random(0, 50);

	serializeJson(data_json, Serial);
	Serial.println();

	delay(100);
}

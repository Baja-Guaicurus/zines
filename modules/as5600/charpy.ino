/*
  arquivo: charpy.ino
  autor: ephiguxta
  propósito: obter dados de ângulo em uma equipamento para ensaio
             de impacto de charpy
  url: 

  README: esse código foi testado em um Arduino Mega 2560, as portas
  de SDA e SCL já estão expostas na placa, basta conectá-las.
*/

// link: https://github.com/RobTillaart/AS5600
#include <AS5600.h>

AS5600 sensor;

uint16_t raw_angle;
uint16_t degrees;

// serve para gravar a posição inicial do martelo,
// essa posição é quando o martelo fica parado na
// trava
uint16_t init_pos;

void setup() {
  Serial.begin(115200);
  while(Serial.available());

  Wire.begin();

  sensor.begin();
  sensor.setDirection(AS5600_CLOCK_WISE);

  delay(5000);


}

void loop() {
  Serial.print(millis());
  Serial.print("\t");

  uint16_t raw_angle = sensor.rawAngle();
  uint16_t degrees = raw_angle * AS5600_RAW_TO_DEGREES;

  Serial.print(degrees);
  Serial.println("°");

  delay(32);
}

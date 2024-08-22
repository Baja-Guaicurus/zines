arduino-cli compile --fqbn esp32:esp32:esp32 $1/ && \
arduino-cli upload -p /dev/ttyUSB0 --fqbn esp32:esp32:esp32 $1/ 


from serial import Serial
from datetime import datetime

port = "/dev/ttyUSB0"
baud_rate = 19600

lora_slave = Serial(port, baud_rate)

while True:
    print(f"Listening for incoming data..")
    incoming = lora_slave.readline()
    hex_value = incoming[0]
    print(f"{hex_value} dBm")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", 'a') as log:
        log.write(f"{timestamp} : {hex_value} dBm\n")

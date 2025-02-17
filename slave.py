from serial import Serial

port = "/dev/ttyUSB0"
baud_rate = 19600

lora_slave = Serial(port, baud_rate, timeout=10)

while True:
    print(f"Listening for incoming data..")
    incoming = lora_slave.readline()
    hex_value = incoming[0]
    print(hex_value)

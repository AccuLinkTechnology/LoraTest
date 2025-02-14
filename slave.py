from serial import Serial

port = "/dev/ttyUSB0"
baud_rate = 19600

lora_slave = Serial(port, baud_rate)


while True:
    print("Listening for incoming data..")
    incoming = lora_slave.readline().decode('ascii').rstrip()
    print(f"[MASTER]: {incoming}")


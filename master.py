#Lora Testing 
import time
from serial import Serial

# usb_num = input("Enter USB Number. e.g ttyUSBX\n")

# lora = Serial(port=f"/dev/ttyUSB{usb_num}")

port = "/dev/ttyUSB2"
baud_rate = 19600
lora = Serial(port, baud_rate)
# ===========   ===========   ===========   ===========   ===========

command = "ER_CMD#B?"
lora.write(command.encode() + b'\n')

# ACK = "ACK"
# lora.write(ACK.encode())

print(lora.readline().decode('ascii').rstrip())

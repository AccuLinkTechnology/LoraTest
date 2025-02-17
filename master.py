#Lora Testing 
import time
from serial import Serial

# usb_num = input("Enter USB Number. e.g ttyUSBX\n")

# lora = Serial(port=f"/dev/ttyUSB{usb_num}")

port = "/dev/ttyUSB0"
baud_rate = 19600
lora = Serial(port, baud_rate)

def send_command(command):
    lora.write(command.encode())
    
# ===========   ===========   ===========   ===========   ===========
while True:
    send_command("\n")
    time.sleep(3)

#send_command("ER_CMD#T8")
#print(lora.readline())

#send_command("ACK")
#print(lora.readline())


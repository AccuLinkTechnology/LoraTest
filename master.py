#Lora Testing 
from serial import Serial

usb_num = input("Enter USB Number. e.g ttyUSBX\n")

lora = Serial(port=f"/dev/ttyUSB{usb_num}")

lora.write("Checken")
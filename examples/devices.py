from pyneltuya.five import devices
from time import sleep

dev1 = devices.Device1D("YOUR_DEVICES_ID", "YOUR_DEVICES_IP", "YOUR_DEVICES_LOCAL_KEY", 12) # Replace 12 with your actualy device's max

dev1.connect()
dev1.on()

dev1.RGB_fill(255, 0, 0)
sleep(1.5)

dev1.W_fill(100)
sleep(1.5)

dev1.RGB_fill(0, 255, 0)
sleep(1.5)

for segment_id in range(1, 13): # Replace 13 with your actualy device's max + 1
    dev1.RGB_tile(segment_id, 0, 0, 255)
    sleep(1.5)

dev1.off()
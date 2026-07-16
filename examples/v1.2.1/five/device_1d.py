from pyneltuya.five import devices
from time import sleep

dev1 = devices.Device1D("YOUR_DEVICES_ID", "YOUR_DEVICES_IP", "YOUR_DEVICES_LOCAL_KEY", 12) # Replace 12 with your actualy device's max

dev1.connect()
dev1.on()

dev1.RGB_fill(255, 0, 0)
sleep(2)

dev1.W_fill(100)
sleep(2)

dev1.RGB_fill(0, 255, 0)
sleep(2)

for segment_id in range(1, 10): # Replace 13 with your actualy device's max + 1
    dev1.RGB_tile(segment_id, 0, 0, 255)
    sleep(1)

dev1.RGB_fill(0, 0, 0)

sleep(2)

dev1.RGB_fill(128, 128, 128)

sleep(2)

dev1.RGB_fill(255, 255, 255)

sleep(2)


dev1.RGB_fill(0, 0, 128)

sleep(2)

dev1.RGB_fill(0, 0, 255)

sleep(2)


dev1.RGB_fill(128, 128, 0)

sleep(2)

dev1.RGB_fill(255, 255, 0)

sleep(2)


dev1.off()
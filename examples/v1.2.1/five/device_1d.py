from pyneltuya.five import devices
from time import sleep

dev1 = devices.Device1D("bf447b413b8dbafd67wv2m", "192.168.1.124", "?V4pd.11Gi)[.NmI", 12)


dev1.connect()
dev1.on()

dev1.RGB_fill(255, 0, 0)
sleep(2)

dev1.W_fill(100)
sleep(2)

dev1.RGB_fill(0, 255, 0)
sleep(2)

for segment_id in range(1, 10):
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
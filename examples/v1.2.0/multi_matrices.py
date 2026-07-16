from pyneltuya.five import devices, matrices
from time import sleep

matrix1 = matrices.SimpleMultiMatrix([devices.Device1D("YOUR_DEVICES_ID", "YOUR_DEVICES_IP", "YOUR_DEVICES_LOCAL_KEY", 12), devices.Device1D("YOUR_DEVICES_ID", "YOUR_DEVICES_IP", "YOUR_DEVICES_LOCAL_KEY", 12)], [ # Replace 12 with your actualy device's max
    [(1, 7), (1, 8), (0, 8), (0, 7)],
    [(1, 6), (1, 5), (0, 5), (0, 6)],
    [(1, 3), (1, 4), (0, 4), (0, 3)],
    [(1, 2), (1, 1), (0, 1), (0, 2)]
])

matrix1.device(0).connect()
matrix1.device(1).connect()
matrix1.device(0).on()
matrix1.device(1).on()

matrix1.show_image("images.jpeg") # Replace images.jpeg with your actualy image path

sleep(2)

matrix1.set_pixel(1, 1, 255, 255, 255)

sleep(2)

matrix1.device(0).off()
matrix1.device(1).off()
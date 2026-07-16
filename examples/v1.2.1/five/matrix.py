from pyneltuya.five import devices, matrices
from time import sleep

mat1 = matrices.Matrix(devices.Device1D("YOUR_DEVICES_ID", "YOUR_DEVICES_IP", "YOUR_DEVICES_LOCAL_KEY", 12), [ # Replace 12 with your actualy device's max
    [8, 7],
    [5, 6],
    [4, 3],
    [1, 2]
])

mat1.device().connect()
mat1.device().on()

mat1.show_image("image.png")

sleep(2)

mat1.set_pixel(1, 1, 255, 255, 255) # Replace image.png with your actualy image path

sleep(2)

mat1.device().off()
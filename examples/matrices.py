from pyneltuya.five import devices, matrices
from time import sleep

matrix1 = matrices.SimpleMatrix(devices.Device1D("YOUR_DEVICES_ID", "YOUR_DEVICES_IP", "YOUR_DEVICES_LOCAL_KEY", 12), [ # Replace 12 with your actualy device's max
    [2, 1],
    [3, 4]
])

matrix1.device().connect()
matrix1.device().on()

matrix1.show(
    [
        [(0, 255, 0), (0, 255, 255)],
        [(0, 255, 255), (0, 0, 255)]
    ]
)

sleep(2)

matrix1.show_image("image.png") # Replace image.png with your actualy image path

sleep(2)

matrix1.set_pixel(1, 1, 255, 255, 255)

sleep(2)

matrix1.device().off()
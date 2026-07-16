from pyneltuya.five import devices, matrices
from time import sleep

mat1 = matrices.Matrix(devices.Device1D("bf447b413b8dbafd67wv2m", "192.168.1.124", "?V4pd.11Gi)[.NmI", 12), [
    [8, 7],
    [5, 6],
    [4, 3],
    [1, 2]
])

mat1.device().connect()
mat1.device().on()

mat1.show_image("image.png")

sleep(2)

mat1.set_pixel(1, 1, 255, 255, 255)

sleep(2)

mat1.device().off()
from pyneltuya.five import devices, matrices
from time import sleep

matrix1 = matrices.MultiMatrix([devices.Device1D("bf447b413b8dbafd67wv2m", "192.168.1.124", "?V4pd.11Gi)[.NmI", 12), devices.Device1D("bf20f2e7e3946d6926rwka", "192.168.1.142", "NN|'a#jFV;i<BzSA", 12)], [
    [(1, 7), (1, 8), (0, 8), (0, 7)],
    [(1, 6), (1, 5), (0, 5), (0, 6)],
    [(1, 3), (1, 4), (0, 4), (0, 3)],
    [(1, 2), (1, 1), (0, 1), (0, 2)]
])

matrix1.device(0).connect()
matrix1.device(1).connect()
matrix1.device(0).on()
matrix1.device(1).on()

matrix1.show_image("images.jpeg")

sleep(4)

matrix1.set_pixel(1, 1, 255, 255, 255)

sleep(2)

matrix1.device(0).off()
matrix1.device(1).off()
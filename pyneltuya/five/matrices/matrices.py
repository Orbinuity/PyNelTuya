from pyneltuya.five.devices import Device1D
from PIL import Image

class Matrix:
    def __init__(self, device:Device1D, matrix:list[list[int]]):
        """
        Use matrix stuff on a 1D Device.

        Args:
            device (Device1D): The device's class.
            matrix (list[list[int]]): The matrix structure.
        """
        self._device = device
        self._matrix = matrix
        self._matrix_x = len(self._matrix[0])
        self._matrix_y = len(self._matrix)
    
    def show(self, pixel_data:list[list[tuple[int]]]):
        """
        Show a whole matrix on the device.

        Args:
            pixel_data (list[list[tuple[int]]]): The matrix light structrue.
        """
        for y in range(len(pixel_data)):
            for x in range(len(pixel_data[y])):
                c = pixel_data[y][x]
                self.set_pixel(x, y, c[0], c[1], c[2])

    def show_image(self, image_path:str):
        """
        Show a image on the device.

        Args:
            image_path (str): The path to the image.
        """
        img = Image.open(image_path).resize((self._matrix_x, self._matrix_y), Image.Resampling.NEAREST).convert("RGB")
        width, height = img.size
        flat_pixels = list(img.getdata())
        self.show([flat_pixels[y * width : (y + 1) * width] for y in range(height)])
    
    def set_pixel(self, x:int, y:int, r:int, g:int, b:int):
        """
        Set a specific pixel.

        Args:
            x (int): The x coordinate. (0-matrix_x)
            y (int): The y coordinate. (0-matrix_y)
            r (int): The red color vlaue. (0-255)
            g (int): The green color vlaue. (0-255)
            b (int): The blue color vlaue. (0-255)
        """
        try:
            if self._matrix[x][y]:
                self._device.RGB_tile(self._matrix[x][y], r, g, b)
        except (KeyError, TypeError):
            print(f"Pixel {x}, {y} does not exist")

    def device(self) -> Device1D:
        """
        Return the device class.

        Returns:
            Device1D: The device class.
        """
        return self._device

class MultiMatrix(Matrix):
    def __init__(self, devices:list[Device1D], matrix:list[list[tuple[int]]]):
        """
        Use matrix stuff on a 1D Device.

        Args:
            devices (list[Device1D]): List of devices.
            matrix (list[list[tuple[int]]]): The matrix structure.
        """
        self.devices = devices
        self._matrix = matrix
        self._matrix_x = len(self._matrix[0])
        self._matrix_y = len(self._matrix)
    
    def set_pixel(self, x:int, y:int, r:int, g:int, b:int):
        """
        Set a specific pixel.

        Args:
            x (int): The x coordinate. (0-matrix_x)
            y (int): The y coordinate. (0-matrix_y)
            r (int): The red color vlaue. (0-255)
            g (int): The green color vlaue. (0-255)
            b (int): The blue color vlaue. (0-255)
        """
        try:
            if self._matrix[x][y]:
                pixel_data = self._matrix[x][y]
                self.devices[pixel_data[0]].RGB_tile(pixel_data[1], r, g, b)
        except (KeyError, TypeError):
            print(f"Pixel {x}, {y} does not exist")

    def device(self, index:int) -> Device1D:
        """
        Return the device class.

        Args:
            index (int): The device you want to select.

        Returns:
            Device1D: The selected device class.
        """
        return self.devices[index]
from pyneltuya.five.devices import Device1D
from PIL import Image

class SimpleMatrix:
    def __init__(self, device:Device1D, matrix:list[list[int]]):
        """
        Use matrix stuff on a 1D Device.

        Args:
            device (Device1D): The device's class.
            matrix (list[list[int]]): The matrix structure.
        """
        self._device = device
        self._matrix = matrix
        self._matrix_x = len(self._matrix)
        self._matrix_y = len(self._matrix[0])
    
    def show(self, pixel_data:list[list[tuple[int]]]):
        """
        Show a whole matrix on the device.

        Args:
            pixel_data (list[list[tuple[int]]]): The matrix light structrue.
        """
        if len(pixel_data) != self._matrix_x: raise ValueError(f"Expected pixel_data to be a size of {self._matrix_x} not {len(pixel_data)}.")
        for y in range(len(pixel_data)):
            if len(pixel_data[y]) != self._matrix_y: raise ValueError(f"Expected list {y+1} in pixel_data to be a size of {self._matrix_y} not {len(pixel_data[y])}.")
            for c in range(len(pixel_data[y])):
                if len(pixel_data[y][c]) != 3: raise ValueError(f"Expected tuple {c+1} in list {y+1} in pixel_data to be a size of 3 (R, G, B) not {len(pixel_data[y][c])}.")

        for x in range(len(pixel_data)):
            for y in range(len(pixel_data[x])):
                c = pixel_data[x][y]
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
        self._device.RGB_tile(self._matrix[x][y], r, g, b)

    def device(self):
        """
        Return the device class.

        Returns:
            The device class.
        """
        return self._device
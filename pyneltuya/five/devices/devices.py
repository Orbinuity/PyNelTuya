from abc import ABC, abstractmethod
from typing import final
from time import sleep
import tinytuya
import colorsys
import base64

class Device(ABC):
    def __init__(self, device_id:str, address:str, local_key:str):
        """
        This is a parent class used to make devices, use this call only if chiled classes dont work for you.

        Args:
            device_id (str): The device id of the tuya device.
            address (str): The local ip address of the tuya device.
            local_key (str): The local key the the tuya device.
        """
        self._device = tinytuya.Device(dev_id=device_id, address=address, local_key=local_key, version=3.5)
        self._device.set_socketPersistent(True)
        self._current_mode = ""

    @final
    def connect(self):
        """
        Savly connect with the device.
        """
        self._device.status()

    @final
    def send_tuya(self, dp_id:int, dp_value):
        """
        Send custom dp data to the tuya device.

        Args:
            dp_id (int): The dp id.
            dp_value (any): The value you want tot set it to.
        """
        self._device.set_value(dp_id, dp_value)
    
    @final
    def on(self):
        """
        Turn on the whole device.
        """
        self.send_tuya(20, True)

    @final
    def off(self):
        """
        Turn off and clean up the whole device.
        """
        self.RGB_fill(0, 0, 0)
        self.send_tuya(20, False)
    
    @final
    def mode(self, mode:str, force:bool=False):
        """
        Set the device's mode.

        Args:
            mode (str): The mode id: white, colour, scene or music (Check you devises DP info to see if there are others).
            force (bool): Normaly False turn on only if other apps change the mode.
        """
        if self._current_mode != mode or force:
            self.send_tuya(21, mode)
            self._current_mode = mode
            sleep(0.15)
    
    @abstractmethod
    def RGB_fill(self):
        pass

    @abstractmethod
    def RGB_tile(self):
        pass

    @abstractmethod
    def W_fill(self):
        pass
    
    @abstractmethod
    def scene(self):
        pass

    @abstractmethod
    def music(self):
        pass


class Device1D(Device):
    def __init__(self, device_id:str, address:str, local_key:str, max_tiles:int):
        """
        Control a light device that goes in a chain (1D).

        Args:
            device_id (str): The device id of the tuya device.
            address (str): The local ip address of the tuya device.
            local_key (str): The local key the the tuya device.
            max_tiles (int): The max amount of tiles your device can handel.
        """
        super().__init__(device_id, address, local_key)
        self._max_tiles = max_tiles

    def RGB_fill(self, r:int, g:int, b:int):
        """
        Set the whole device to a RGB color.

        Args:
            r (int): The red value.
            g (int): The green value.
            b (int): The blue value.
        """
        self.mode("colour")
        h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
        tuya_h = int(h * 360)
        tuya_s = int(s * 1000)
        tuya_v = int(v * 1000)

        payload = bytearray()
        payload.append(0x00)
        payload.append(0x01)
        payload.append((self._max_tiles >> 8) & 0xFF)
        payload.append(self._max_tiles & 0xFF)
        payload.append(0x00)
        payload.append((tuya_h >> 8) & 0xFF)
        payload.append(tuya_h & 0xFF)
        payload.append((tuya_s >> 8) & 0xFF)
        payload.append(tuya_s & 0xFF)
        payload.append((tuya_v >> 8) & 0xFF)
        payload.append(tuya_v & 0xFF)

        b64_payload = base64.b64encode(payload).decode('utf-8')
        self.send_tuya(61, b64_payload)

    def RGB_tile(self, tile_index:int, r:int, g:int, b:int):
        """
        Set a specific tile to a RGB color.

        Args:
            tile_index (int): The tile you want to use (1-max_tiles)
            r (int): The red value.
            g (int): The green value.
            b (int): The blue value.
        """
        self.mode("colour")
        h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
        tuya_h = int(h * 360)
        tuya_s = int(s * 1000)
        tuya_v = int(v * 1000)

        payload = bytearray()

        payload.append(0x00)
        payload.append(0x01)
        payload.append((self._max_tiles >> 8) & 0xFF)
        payload.append(self._max_tiles & 0xFF)

        payload.append(0x01)

        payload.append((tuya_h >> 8) & 0xFF)
        payload.append(tuya_h & 0xFF)
        payload.append((tuya_s >> 8) & 0xFF)
        payload.append(tuya_s & 0xFF)
        payload.append((tuya_v >> 8) & 0xFF)
        payload.append(tuya_v & 0xFF)

        payload.append(0x80 | 1)

        payload.append(tile_index)

        b64_payload = base64.b64encode(payload).decode('utf-8')
        self.send_tuya(61, b64_payload)

    def W_fill(self, brightness:int):
        """
        Use the device's white mode and set the brightness.

        Args:
            brightness (int): How intense to set the white (0-100)
        """
        self.mode("white")
        self.send_tuya(22, brightness*10)

    def scene(self, scene_id:str):
        """
        Play a specific scene.

        Args:
            scene_id (str): The scene id (eg "ARcDXl5gAABkADgvAB5cANVFARpk")
        """
        self.mode("scene")
        self.send_tuya(51, scene_id)
    
    def music(self):
        """
        Start light control based on music.
        """
        self.mode("music")
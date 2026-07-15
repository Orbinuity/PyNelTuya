import tinytuya
import time

DEVICE_IP = "192.168.1.124"
DEVICE_ID = "bf447b413b8dbafd67wv2m"
DEVICE_KEY = "?V4pd.11Gi)[.NmI"

while True:
    try:
        device = tinytuya.Device(DEVICE_ID, DEVICE_IP, DEVICE_KEY, version=3.5)
        device.set_socketPersistent(True)
        
        device.status()
        print("LISTENING LOCAL NETWORK... Keep this script running!")
        print("Now open your Tuya app and change things.")
        
        while True:
            data = device.receive()
            if data and 'dps' in data:
                print(f"\nCAUGHT A DATA UPDATE -> {data['dps']}")
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nStopping spy script.")
        break
    except Exception as e:\
        time.sleep(1)
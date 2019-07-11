import serial
import time
import glob

BAUD               = 57600
SERIAL_TIMEOUT     = 0
RECONNECT_ATTEMPTS = 3

class Radio:
    """Initialize and handle communications between telemetry radios.
    """

    def __init__(self, port=None, baud=BAUD, timeout=SERIAL_TIMEOUT):
        self.serial_port = None

        if port is not None:
            self._initialize_telemetry(port, baud, timeout)
        else:
            self._find_mac_radio()

    def write(self, data):
        self.serial_port.write(data)

    def read(self, n_bytes=None):
        if n_bytes is None: n_bytes = self.bytes_available()
        return self.serial_port.read(n_bytes)

    def bytes_available(self):
        return self.serial_port.inWaiting()

    # Try to connect to radio at given port
    def _initialize_telemetry(self, port=None, baud=BAUD, timeout=SERIAL_TIMEOUT):
        attempts = 0
        while True:
            try:
                self.serial_port = serial.Serial(port=port, baudrate=baud, timeout=timeout)
                print("Initialized telemetry radio.")
                return True
            except serial.serialutil.SerialException:
                if attempts > RECONNECT_ATTEMPTS:
                    return False
                else:
                    print("Radio not found, trying again. Did you run as `sudo`?")
                    time.sleep(1)
                    attempts += 1

    def _find_mac_radio(self):
        devices = glob.glob('/dev/tty.usbserial*')
        for device in devices:
            if self._initialize_telemetry(device):
                return

    def close(self):
        self.serial_port.close()
        

if __name__ == '__main__':
    r = Radio()
    while True:
        r.write(0)
        time.sleep(0.1)

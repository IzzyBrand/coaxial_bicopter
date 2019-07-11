import time
import RTIMU
import numpy as np
from multiprocessing import Process, Array

class IMU:
    def __init__(self):
        self.data = Array('f', np.zeros(3, dtype=float))
        self.process = Process(target=self.spin, name='IMU', args=(self.data,))

        self.process.start()
        
    def read(self):
        if self.data.acquire():
            to_return = np.array(self.data[:3])
            self.data.release()
        return to_return

    def spin(self, data):
        settings = RTIMU.Settings('RTIMULib')
        imu = RTIMU.RTIMU(settings)
        print('IMU init' if imu.IMUInit() else 'IMU failed to init!')
        imu.setSlerpPower(0.02)
        imu.setGyroEnable(True)
        imu.setAccelEnable(True)
        imu.setCompassEnable(True)
        poll_interval = imu.IMUGetPollInterval()/1000.

        while True:
            if imu.IMURead():
                raw = imu.getFusionData()
                if data.acquire(False):
                    data[:] = raw[:]
                    data.release()

                time.sleep(poll_interval)


if __name__ == '__main__':
    imu = IMU()

    while True:
        print(imu.read())
        time.sleep(0.01)



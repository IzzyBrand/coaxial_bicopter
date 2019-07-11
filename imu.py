import time
import RTIMU

class IMU:
    def __init__(self):
        self.settings = RTIMU.Settings('RTIMULib')
        self.imu = RTIMU.RTIMU(self.settings)
        print('IMU init' if self.imu.IMUInit() else 'IMU failed to init!')
        self.imu.setSlerpPower(0.02)
        self.imu.setGyroEnable(True)
        self.imu.setAccelEnable(True)
        self.imu.setCompassEnable(True)

    def read(self):
        return self.imu.getFusionData() if self.imu.IMURead() else None


if __name__ == '__main__':
    imu = IMU()



    while True:
        data = imu.read()
        if data is not None:
            print(data)



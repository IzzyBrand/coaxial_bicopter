import array
import numpy as np
import time

from imu import IMU
from pid import PID
from radio import Radio
from servos import Servos

# r = Radio('/dev/ttyUSB0')
# while True:
#   if r.bytes_available() > 16:
#       data = r.read()
#       print(data.decode())
# r.close()

if __name__ == '__main__':
    imu = IMU()
    servos = Servos()

    pid_roll  = PID(600., 0., 0., control_range=[-250, 250])
    pid_pitch = PID(-600., 0., 0., control_range=[-250,250])
    pid_yaw   = PID(10., 0., 0)
    pids = [pid_roll, pid_pitch, pid_yaw]

    rpy = np.zeros(3)
    sp_rpy = np.zeros(3)
    cmd = np.array([1000, 1000, 1500, 1500])

    throttle = 1100

    tt = t = time.time()
    running = True
    while running:
        t = time.time()
        dt = t - tt
        tt = t

        # calculate the error from the set_point
        rpy[[1, 0, 2]] = imu.read()
        err_rpy = sp_rpy - rpy

        # run each of the pid controllers
        cmd_rpy = [pid.step(e, dt) for pid, e in zip(pids, err_rpy)]

        # copy the rates into the servo array
        cmd[0] = throttle #+ cmd_rpy[2]
        cmd[1] = throttle #- cmd_rpy[2]
        cmd[2] = 1555 + int(cmd_rpy[0])
        cmd[3] = 1460 + int(cmd_rpy[1]) 

        # and write the command to the servos
        print(dt)
        servos.write(cmd)

        # wait the remaining time to keep the loop rate constant
        # elapsed_time = time.time() - start_time
        # remaining_time = dt - elapsed_time
        # if remaining_time > 0:
        #     time.sleep(remaining_time)
        # else:
        #     print('Slipping {}'.format(remaining_time))


    servos.stop_servod()
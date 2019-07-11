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

    pid_roll  = PID(400., 0., 0., control_range=[-150, 150])
    pid_pitch = PID(-400., 0., 0., control_range=[-150,150])
    pid_yaw   = PID(0., 0., 0.)
    pids = [pid_roll, pid_pitch, pid_yaw]

    rpy = np.zeros(3)
    sp_rpy = np.zeros(3)
    cmd = np.array([1000, 1000, 1500, 1500])

    tt = t = time.time()
    running = True
    while running:
        data = imu.read()
        if data is not None:
            # get the elapsed time
            t = time.time()
            dt = t - tt
            if dt < 1/10: continue
            tt = t

            # calculate the error from the set_point
            rpy[[1, 0, 2]] = data
            err_rpy = sp_rpy - rpy

            # run each of the pid controllers
            cmd_rpy = [pid.step(e, dt) for pid, e in zip(pids, err_rpy)]

            # copy the rates into the servo array
            cmd[2] = int(cmd_rpy[0]) + 1500
            cmd[3] = int(cmd_rpy[1]) + 1500

            # and write the command to the servos
            print(cmd)
            # start_time = time.time()
            # servos.write(cmd)
            # print(time.time() - start_time)


    servos.stop_servod()
import params as p
import numpy as np
import os

class Servos(object):
    def __init__(self):
        self.stop_servod() # kill any running servod processes
        self.start_servod()
        self.servo_scale = 250

    def start_servod(self):
    	os.system('sudo servod --p1pins="{},{},{},{}" --step-size=2'.format(*p.servo_pins))

    def stop_servod(self):
        os.system("sudo killall servod")

    def write(self, cmd=np.zeros_like(p.servo_pins)):
        f = open('/dev/servoblaster', 'w')
        for i, c in enumerate(np.clip(cmd, 1000, 2000)):
            # os.system("echo {}={}us > /dev/servoblaster".format(i, c))
            f.write('{}={}us\n'.format(i, c))
        f.close()

if __name__ == '__main__':
    from time import sleep

    s = Servos()
    cmd = np.array([1000, 1000, 1500, 1500])

    for j in range(10):
        print(j)
        for i in np.linspace(1300, 1800, 100):
            cmd[2] = int(i)
            s.write(cmd)
            sleep(0.5/100)

    s.stop_servod()
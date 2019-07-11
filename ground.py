import numpy as np
import pygame
import time
import array

from radio import Radio


 
pygame.init()

# Loop until the user clicks the close button.
done = False
 
vals = np.zeros(4)

r = Radio()

while not done:
    # EVENT PROCESSING STEP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.JOYAXISMOTION:
            axis = event.dict['axis']
            val = event.dict['value']
            vals[axis] = val

    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    

    # print((np.clip(vals + 1, 0, 2)/2 * 128).astype(int))
    byte_string = str(vals).encode()
    print(byte_string.decode())
    # r.write(byte_string)
    time.sleep(0.05)

pygame.quit()
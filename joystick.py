"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Show everything we can pull off the joystick
"""
import pygame
 
 
pygame.init()
 
# Set the width and height of the screen [width,height]
# size = [500, 700]
# screen = pygame.display.set_mode(size)
 
# pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Initialize the joysticks
pygame.joystick.init()
 
 
# -------- Main Program Loop -----------
while not done:
    # EVENT PROCESSING STEP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN
        # JOYBUTTONUP JOYHATMOTION
        print(event.dict)
        # if event.type == pygame.JOYBUTTONDOWN:
        #     print("Joystick button pressed.")
        # if event.type == pygame.JOYBUTTONUP:
        #     print("Joystick button released.")
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # screen.fill(WHITE)
    # textPrint.reset()
 
    # Get count of joysticks
    # joystick_count = pygame.joystick.get_count()
 
    # print("Number of joysticks: {}".format(joystick_count))
    # textPrint.indent()
 
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    # axes = joystick.get_numaxes()
    # # For each joystick:
    # while True:
         
    #     # Get the name from the OS for the controller/joystick
    #     # name = joystick.get_name()
    #     # print("Joystick name: {}".format(name))
 
    #     # # Usually axis run in pairs, up/down for one, and left/right for
    #     # # the other.
        
    #     # print("Number of axes: {}".format(axes))
 
    #     for i in range(axes):
    #         axis = joystick.get_axis(i)
    #         print("Axis {} value: {:>6.3f}".format(i, axis))
 
        # buttons = joystick.get_numbuttons()
        # print("Number of buttons: {}".format(buttons))
 
        # for i in range(buttons):
        #     button = joystick.get_button(i)
        #     print("Button {:>2} value: {}".format(i, button))
 
        # # Hat switch. All or nothing for direction, not like joysticks.
        # # Value comes back in an array.
        # hats = joystick.get_numhats()
        # print("Number of hats: {}".format(hats))
 
        # for i in range(hats):
        #     hat = joystick.get_hat(i)
        #     print("Hat {} value: {}".format(i, str(hat)))
 
 
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
    # Go ahead and update the screen with what we've drawn.
    # pygame.display.flip()
 
    # Limit to 60 frames per second
    # clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

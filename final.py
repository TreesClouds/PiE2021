# MOTOR IDS
KOALA_BEAR = "6_1"
LINE_FOLLOWER = "2_3"
ARM_MOTOR = "6_2"


def drive(left, right):
    if left > 1:
        left = 1
    if right > 1:
        right = 1
    if left != 0 and right != 0:
        print(f"Driving: {round(left, 2)}, {round(right, 2)}")
    Robot.set_value(KOALA_BEAR, "velocity_b", left)
    Robot.set_value(KOALA_BEAR, "velocity_a", right)

def autonomous_setup():
    Robot.set_value(KOALA_BEAR, "pid_enabled_a", False)
    Robot.set_value(KOALA_BEAR, "pid_enabled_b", False)
    Robot.set_value(KOALA_BEAR, "invert_a", True) # right motor initial inversion state
    Robot.set_value(KOALA_BEAR, "invert_b", False) # left motor initial inversion state
    Robot.set_value(ARM_MOTOR, "invert_b", False) # arm motor initial inversion state

def autonomous_main():
#     left = Robot.get_value(LINE_FOLLOWER, "left")
#     center = Robot.get_value(LINE_FOLLOWER, "center")
#     right = Robot.get_value(LINE_FOLLOWER, "right")
    
#     if center == 1:
#         if abs(right - left) < 0.1:
#             drive(1, 1)
#         else:
#             drive(1.2*right, 1.2*left)
#     elif right > left:
#         drive(0.6, -0.4)
#     elif right < left:
#         drive(-0.4, 0.6)

def arm_code():
    while True:
        arm = 0
        if Keyboard.get_value("up_arrow"):
            arm += 0.04
        if Keyboard.get_value("down_arrow"):
            arm -= 0.04
        Robot.set_value(ARM_MOTOR, "velocity_b", arm)
    
def teleop_setup():
    Robot.run(arm_code)

def teleop_main():
    left, right = 0, 0
    if Keyboard.get_value("w"):
        left += 1
    if Keyboard.get_value("s"):
        left -= 1
    if Keyboard.get_value("p"):
        right += 1
    if Keyboard.get_value("l"):
        right -= 1
    drive(left, right)

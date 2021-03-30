def drive(left, right):
    left = left if left <= 1 else 1
    right = right if right <= 1 else 1
    print(f"Driving: {round(left, 2)}, {round(right, 2)}")
    Robot.set_value("left_motor", "duty_cycle", -left)
    Robot.set_value("right_motor", "duty_cycle", right)

def autonomous_setup():
    pass

def autonomous_main():
    left = Robot.get_value("line_follower", "left")
    center = Robot.get_value("line_follower", "center")
    right = Robot.get_value("line_follower", "right")
    
    if Robot.get_value("limit_switch", "switch0"):
        Robot.pick_up()
    if center == 1:
        if abs(right - left) < 0.1:
            drive(1, 1)
        else:
            drive(1.2*right, 1.2*left)
    elif right > left:
        drive(0.6, -0.4)
    elif right < left:
        drive(-0.4, 0.6)
    
    
def teleop_setup():
    pass

def teleop_main():
    Robot.set_value("left_motor", "duty_cycle", -Gamepad.get_value("joystick_left_y"))
    Robot.set_value("right_motor", "duty_cycle", Gamepad.get_value("joystick_right_y"))

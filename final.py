# MOTOR IDS
KOALA_BEAR = "koala_bear"
LINE_FOLLOWER = "line_follower"
ARM_MOTOR = "arm_motor"

# ARM POSITION TARGETS
lower_target = 25
upper_target = 75

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
    Robot.set_value(ARM_MOTOR, "enc_b", 0)
    Robot.set_value(KOALA_BEAR, "invert_a", False) # right motor initial inversion state
    Robot.set_value(KOALA_BEAR, "invert_b", True) # left motor initial inversion state
    Robot.set_value(ARM_MOTOR, "invert_b", False) # arm motor initial inversion state

def autonomous_main():
    left = Robot.get_value("line_follower", "left")
    center = Robot.get_value("line_follower", "center")
    right = Robot.get_value("line_follower", "right")
    
    if center == 1:
        if abs(right - left) < 0.1:
            drive(1, 1)
        else:
            drive(1.2*right, 1.2*left)
    elif right > left:
        drive(0.6, -0.4)
    elif right < left:
        drive(-0.4, 0.6)

def arm_code():
    target = lower_target
    while True:
        position = Robot.get_value(ARM_MOTOR, "enc_b")
        if Keyboard.get_value("down_arrow"):
            text = "LOWER"
            target = lower_target
        elif Keyboard.get_value("up_arrow"):
            text = "UPPER"
            target = upper_target
        
        if position > target:
            Robot.set_value(ARM_MOTOR, "velocity_b", -0.5)
            print(f"Moving arm from {posititon} to {text} target.")
        elif target > position:
            Robot.set_value(ARM_MOTOR, "velocity_b", 0.5)
            print(f"Moving arm from {posititon} to {text} target.")
        else:
            Robot.set_value(ARM_MOTOR, "velocity_b", 0)
            print(f"Arm is at {text} target.")

def config():
    while True:
        if Keyboard.get_value("1"): # Left Motor Inversion Key
            Robot.set_value(KOALA_BEAR, "invert_b", not Robot.get_value(KOALA_BEAR, "invert_b"))
        if Keyboard.get_value("2"): # Right Motor Inversion Key
            Robot.set_value(KOALA_BEAR, "invert_a", not Robot.get_value(KOALA_BEAR, "invert_a"))
        if Keyboard.get_value("3"): # Arm Motor Inversion Key
            Robot.set_value(ARM_MOTOR, "invert_b", not Robot.get_value(ARM_MOTOR, "invert_b"))
    
def teleop_setup():
    Robot.run(arm_code)
    Robot.run(config)

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
    
def pending_machine(num):
    if num == 1:
        print('ampharos')
    elif num == 2:
        print('blastoise')
    elif num == 3:
        print('cyndaquil')
    elif num == 4:
        print('dewgong')
    elif num < 1:
        print('grimer')
    else:
        print('Not accepted')
    pass


def scramble(randomWord, letter):
    before, after = [], []
    for character in randomWord:
        lchar = character.lower()
        llet = letter.lower()
        if lchar == llet or min(lchar, llet) == lchar:
            before.append(character)
        else:
            after.append(character)
    return before, after


def wacky_numbers(carolNum, oskiNum, numrounds):
    carolPoint, oskiPoint = 0, 0
    for rnd in range(numrounds):
        if rnd % carolNum == 0:
            carolPoint += rnd
        if rnd % oskiNum == 0:
            oskiPoint += rnd
    if carolPoint == oskiPoint:
        print('Tie')
    elif carolPoint > oskiPoint:
        print('Carol')
    elif oskiPoint > carolPoint:
        print('Oski')
    pass


def double_trouble(randomWord):
    randomList = randomWord.lower().replace(' ', '')
    occurrences, count = 0, {}
    for letter in randomList:
        if letter not in count.keys():
            count[letter] = 1
        else:
            count[letter] += 1
    for letter in count:
        if count[letter] == 2:
            occurrences += 1
    return occurrences


def rotCipher(word1, word2):
    word1, word2 = word1.lower(), word2.lower()
    for letter in word1:
        word1 += letter
        word1 = word1[1:]
        if word1 == word2:
            return True
    return False


def robot_triplet(team_weights, target):
    possibilities = []
    for first in team_weights:
        for second in team_weights:
            for third in team_weights:
                tup = (first, second, third)
                if sum(tup) == target and third > second > first:
                    possibilities.append(tup)
    return possibilities


def reverse_lower(string):
    lis = list(string)
    lower_indexes, lower_characters, index = [], [], 0
    for char in lis:
        if char.islower():
            lower_characters.append(char)
            lower_indexes.append(index)
        index += 1
    lower_characters.reverse()
    index = 0
    for char in lower_characters:
        lis[lower_indexes[index]] = char
        index += 1
    return "".join(lis)


def travel(stations):
    stops, index, gas = 0, 0, stations[0]
    stations = stations[1:]
    while True:
        if index + gas >= len(stations):
            return stops
        elif gas < 1:
            return -1
        possible_stops = stations[index:index + gas]
        best_stop = max(possible_stops)
        gas += best_stop
        index = max([a for a, b in enumerate(possible_stops) if b == best_stop])
        stops += 1

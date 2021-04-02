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

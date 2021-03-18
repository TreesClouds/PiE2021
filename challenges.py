"""This is a document to test your code, please put your functions inside of each function and you can add your own test cases"""

"""
Do not import anything!
"""


def pending_machine(num):
    """
    Take in a number `num`. For each instance, do the following:
    If the number is 1, print ‘ampharos’
    If the number is 2, print ‘blastoise’
    If the number is 3, print ‘cyndaquil’
    If the number is 4 print ‘dewgong’
    If the number is less than 1, print “grimer”
    Otherwise, print “Not accepted”

    Parameters:
    num (int) the number to check
    Returns:
    None

    >>> pending_machine(1)
    ampharos
    >>> pending_machine(2)
    blastoise
    >>> pending_machine(3)
    cyndaquil
    >>> pending_machine(-1)
    grimer
    >>> pending_machine(25)
    Not accepted
    """

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
    """
    Takes in a random word and a random letter from that word, splitting the word into the lists representing the letters before and after `letter` alphabetically and ignoring case.

    Parameters:
    randomWord (str) the word
    letter (char) the letter from the word
    Returns:
    two lists: the first list consists of characters that are alphabetically before or the same as the chosen letter and the second consists of characters that come after the chosen letter (ignoring case).

    >>> scramble("Andrew", "n")
    (['A', 'n', 'd', 'e'], ['r', 'w'])
    >>> scramble("Oski", "k")
    (['k', 'i'], ['O', 's'])
    >>> scramble("Aidan", "A")
    (['A', 'a'], ['i', 'd', 'n'])
    >>> scramble("Jennifer", "r")
    (['J', 'e', 'n', 'n', 'i', 'f', 'e', 'r'], [])
    >>> scramble("Elizabeth", "e")
    (['E', 'a', 'b', 'e'], ['l', 'i', 'z', 't', 'h'])
    """

    before, after = [], []
    for character in randomWord:
        lchar = character.lower()
        llet = letter.lower()
        if lchar == llet or min(lchar, llet) == lchar:  # checking if 'lchar' is or is alphabetically before 'llet'
            before.append(character)
        else:
            after.append(character)
    return before, after


def wacky_numbers(carolNum, oskiNum, numrounds):
    """
    Carol Christ and Oski are battling it out for Cal dominance, they agree to a number battle in the end. These are the rules: each party will receive a random
    number, and the game has a random number of rounds. On each round, if the round number is divisible by a player random number, then player with that number scores that number of points. Print either “Carol”, “Oski” for the person who has the most points or output a “Tie” if there is a tie.

    Parameters:
    carolNum (int) Number selected by Carol Christ
    oskiNum (int) Number selected by Oski
    numrounds (int) The number of rounds
    Returns:
    None

    >>> wacky_numbers(2, 3, 5) # carol=2+4=6,oski=3. oski is less than carol so Carol wins
    Carol
    >>> wacky_numbers(3, 3, 4)
    Tie
    >>> wacky_numbers(4, 5, 25)
    Carol
    >>> wacky_numbers(4, 3, 12)
    Oski
    >>> wacky_numbers(5, 3, 2)
    Tie
    """

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
    """
    Given a randomWord, return the number of letters that appear exactly twice in the string.

    For example, the word “vitruvius” has a two v’s,two i’s and two u’s so the output value would be 3.

    Parameters:
    randomword (str) Input String to check for double letters
    Returns:
    int The number of letters that occur twice

    >>> double_trouble("What Will Happen?")
    5
    >>> double_trouble("Apple")
    1
    >>> double_trouble("Alabama")
    0
    >>> double_trouble("Vitruvius")
    3
    >>> double_trouble("Succession")
    1
    """

    randomList = randomWord.lower().replace(' ', '')  # lower to ignore case, replace to remove all spaces
    occurrences, count = 0, {}
    for letter in randomList:
        if letter not in count.keys():  # add letter to the count dictionary, if not already done so
            count[letter] = 1
        else:  # add 1 to the letter's count if already in dictionary
            count[letter] += 1
    for letter in count:
        if count[letter] == 2:
            occurrences += 1
    return occurrences


def rotCipher(word1, word2):
    """
    Given two strings, determine if they are rotated versions of each other. A rotated string is defined by all letters in the string being shifted to one direction by a set amount. Capitalization should not
    be a factor.

    Ex. “Hello” shifted to the right by 2 would become “loHel”.
    Return a boolean, true if rather word2 is a rotated version of word1 and false if not.

    Parameters:
    word1(str) The first word
    word2(str) The second word to check if it's rotated version of the first word
    Returns:
    True iff the word1 is a rotated version of word2

    >>> rotCipher("Elephant", "Phantele")
    True
    >>> rotCipher("NonNon", "NonNon")
    True
    >>> rotCipher("Stanfurd", "Furdnsatn")
    False
    >>> rotCipher("Oski", "Kios")
    True
    >>> rotCipher("Berkeley", "Yelekreb")
    False
    """

    word1, word2 = word1.lower(), word2.lower()  # lower to ignore case
    for letter in word1:  # loop for every letter / every possible rotation
        word1 += letter
        word1 = word1[1:]
        if word1 == word2:  # if a rotation matches
            return True
    return False  # after loop, if no rotations matched


def robot_triplet(team_weights, target):
    """
    A robotics competition requires each team of 3 to have a specific total robot weight.
    Given a list of robot weights and a target weight, give all unique triplets that add up to the
    target weight. Each triplet should be a tuple contained in a list. Within a tuple, the elements should be in ascending order.

    Parameters:
    team_weights (list): A sorted list of unique integers
    target (int): The target weight
    Returns:
    List of unique tuples that contain 3 elements each. You may only use each element up to once.

    >>> robot_triplet([1, 2, 3, 4, 5, 6], 15)
    [(4, 5, 6)]
    >>> robot_triplet([1, 2, 3, 4, 5], 13)
    []
    >>> sorted(robot_triplet([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 14))
    [(1, 2, 11), (1, 3, 10), (1, 4, 9), (1, 5, 8), (1, 6, 7), (2, 3, 9), (2, 4, 8), (2, 5, 7), (3, 4, 7), (3, 5, 6)]
    >>> robot_triplet([], 10)
    []
    >>> robot_triplet([1,2,3,4,5], 0)
    []
    """

    possibilities = []
    for first in team_weights:
        for second in team_weights:
            for third in team_weights:
                tup = (first, second, third)
                if sum(tup) == target and third > second > first:  # filtering every possible number combo to fit prompt
                    # could be much more efficient, but these aren't long lists anyways
                    possibilities.append(tup)
    return possibilities


def reverse_lower(string):
    """
    Given a string reverse the order of all lowercase letters found. Do not reverse the order
    of non-lowercase letters. For example, given the string “He!lo.” we would return the string
    “Ho!le.”, moving around only the letters that are lowercase and keeping all other symbols
    constant including numbers, uppercase letters, and other punctuation.

    Parameters:
    string (str): The string to be modified
    Returns:
    Str the modified input string

    >>> reverse_lower('OskI')
    'OksI'
    >>> reverse_lower('PoWeFuL')
    'PuWeFoL'
    >>> reverse_lower('WAHWaSa')
    'WAHWaSa'
    >>> reverse_lower('He!lo.')
    'Ho!le.'
    >>> reverse_lower('NumB3r5')
    'NrmB3u5'
    """

    lis = list(string)
    lower_indexes, lower_characters, index = [], [], 0
    for char in lis:
        if char.islower():
            lower_characters.append(char)  # to create list of the lower characters
            lower_indexes.append(index)  # to create list of the lower characters' indexes
        index += 1
    lower_characters.reverse()  # reverse the order of the lower characters
    index = 0
    for char in lower_characters:
        lis[lower_indexes[index]] = char  # rematch the reversed characters with the indexes
        index += 1
    return "".join(lis)  # rejoin the list to create the word


def travel(stations):
    """
    You are travelling from Cal to Stanford and are given a list of gas stations at 1 mile increments. stations[i] represents the gallons of gas you can get at station i. Each gallon allows you to travel 1 more mile. stations[0] represents the amount of gas that you start with (and does not count as a stop). The last location in stations can be ignored because it is Stanford.

    Determine the minimum amount of stops you can take in order to get to Stanford, the last station. Remember that you can never have a negative amount of gas. If you cannot reach Stanford without violating this condition, return -1.

    Parameters:
    stations (List) The list of stops
    Returns:
    int The minimum number of stops needed to reach Stanford

    >>> travel([2, 3, 1, 1, 4])
    1
    >>> travel([1, 1])
    0
    >>> travel([0, 3, 2])
    -1
    >>> travel([1, 1, 1, 1])
    2
    >>> travel([1, 2, 2, 1, 0, 1])
    2
    """

    stops, index, gas = 0, 0, stations[0]
    stations = stations[1:]  # remove initial amount of gas
    while True:
        if index + gas >= len(stations):  # check if there is enough gas to reach stanford from current location
            return stops
        elif gas < 1:  # check if there is any gas
            return -1
        possible_stops = stations[index:index + gas]  # create list of possible stops with the current amount of gas
        best_stop = max(possible_stops)  # find best gas station within the possible stops
        gas += best_stop
        index = max([a for a, b in enumerate(possible_stops) if b == best_stop])  # find index of best stop, farthest if there are multiple
        stops += 1

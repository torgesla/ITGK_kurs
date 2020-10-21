# Constants
NTNU_scores = (89, 77, 65, 53, 41, 0)
NTNU_letters = ('A', 'B', 'C', 'D', 'E', 'F')
TASKS = ('1', '2a', '2b', '2c', '3a', '3b', '3c', '3d', '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h')
WEIGHTS = (25, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)


def makeArray(Numbers, Texts):  # Create 2d list from two tuples / lists / iterables
    return_list = []
    for i in range(len(Numbers)):
        new_element = [Numbers[i], Texts[i]]
        return_list.append(new_element)
    return return_list


def computeScore(Points, WEIGHTS):  # Returns score in percent of max
    final_score = 0
    max_score = 0
    for i in range(len(Points)):
        final_score += Points[i] * WEIGHTS[i]
        max_score += 10 * WEIGHTS[i]
    return 100 * final_score / max_score  # Percent score


def score2Letter(score, limitLetters):  # Assumes that limitLetters are sorted in descending order
    # limitLetters = limitLetter.sort(), hvis sortere etter 1. element
    # limitLetters = limitLetter.sort(key = lambda limitLetter: limitLetter[1]) for å sortere etter andre element
    for limit_letter in limitLetters:
        limit_score = limit_letter[0]
        letter = limit_letter[1]
        if(score >= limit_score):
            return letter


def addCandidate(candidateNumber, Scores, WEIGHTS):
    candidate_string = ''
    candidate_string += str(candidateNumber) + '\t'
    for score_per_task in Scores:
        candidate_string += str(score_per_task) + '\t'
    candidate_string += str(computeScore(Scores, WEIGHTS)) + '\n'

    try:
        fil = open(minnepinnePath + 'eksamen.txt', mode='a', encoding='utf-8')
        fil.write(candidate_string)
        fil.close()
    except FileNotFoundError as error_message:
        print(error_message)


def readResultFile(filename):
    with open(filename, mode='r', encoding='utf-8') as fil:
        file_content = fil.readlines()  # List of strings
    Table = []
    for line in file_content:
        line_content = line.strip().split('\t')  # List of strings
        record = []
        for number in line_content:
            try:  # Fails if string doesn't represent an integer (last column)
                record.append(int(number))
            except ValueError:
                record.append(float(number))
        Table.append(record)
    return Table


def printTable(Table):  # Prints table in a nice way
    for row in Table:
        print(row)


def allUnique(file_content):  # returns False if not all unique, else True
    isOK = True
    unique_cand_numbers = []
    for record in file_content:
        cand_number = record[0]
        if(cand_number in unique_cand_numbers):
            print(f'ERROR: Candidate {cand_number} appears more than once!')
            isOK = False
        else:
            unique_cand_numbers.append(cand_number)
    return isOK


def correctPartScores(file_content):  # returns False if any part score is wrong, else True
    isOK = True
    for record in file_content:  # Iterate through every except cand and final_score
        cand_number = record[0]
        for cell in record[1:-1]:  # Excludes cand_number and final score
            if(cell < 0 or cell > 10):
                print(f'ERROR: Candidate {cand_number} scores are not between 0-10')
                isOK = False
    return isOK


def correctTotalScore(file_content):  # returns False if total score is wrong, else True
    isOK = True
    for record in file_content:
        cand_number = record[0]
        score_in_record = record[-1]
        correct_score = computeScore(record[1:-1], WEIGHTS)  # Excludes cand_number and final score
        if(score_in_record != correct_score):
            print(f'ERROR: Candidate {cand_number} has wrong total score!')
            isOK = False
    return isOK


def checkResultOK(filename, WEIGHTS):  # checks if all requirements are met
    isOK = True
    file_content = readResultFile(filename)
    isOK = allUnique(file_content)
    isOK = correctPartScores(file_content)
    isOK = correctTotalScore(file_content)
    return isOK


def listAll(filename, limitLetters):
    cand_score_letter = []
    file_content = readResultFile(filename)
    for record in file_content:
        cand_number = record[0]
        total_score = record[-1]
        letter_grade = score2Letter(total_score, limitLetters)
        cand_score_letter.append([cand_number, total_score, letter_grade])
    printTable(cand_score_letter)
    return len(cand_score_letter)


# 4a #
limitLetters = makeArray(NTNU_scores, NTNU_letters)
# print(limitLetters)

# 4b #
weightTasks = makeArray(WEIGHTS, TASKS)
# print(weightTasks)

# 4c #
Points = [10, 0, 0, 0, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0]
# print('Task 4c',computeScore(Points, WEIGHTS))

# 4d #
# print('Task 4d', score2Letter(88.9, limitLetters))

# 4e #
minnepinnePath = ''
addCandidate(12345, Points, WEIGHTS)
Points2 = [0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 4, 10, 10, 10, 10, 10]
addCandidate(33322, Points2, WEIGHTS)
# minnepinnePath = 'E:\'; addCandidate(12492,[0,10,10,10,0,0,0,0,0,10,10,10,10,10,10,10],WEIGHTS)

# 4f #
#Table = readResultFile('eksamen.txt')
# printTable(Table)
# 4g #
#print(checkResultOK('eksamen.txt', WEIGHTS))

# 4h #
listAll('eksamen.txt', limitLetters)

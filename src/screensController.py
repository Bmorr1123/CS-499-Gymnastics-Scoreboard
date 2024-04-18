import arenaScreen
import scorekeeperScreen

global aScreen
global sScreen
global displayLogo
global displayOrder
global displaySV
global displayJudges
global meetFormat
global competingSchools
scores1 = []
meetScores1 = 0
scores2 = []
meetScores2 = 0
scores3 = []
meetScores3 = 0
scores4 = []
meetScores4 = 0

name1s = "Keee"
class1s = ""
major1s = ""
avg1s = ""

name2s = ""
class2s = ""
major2s = ""
avg2s = ""

name3s = ""
class3s = ""
major3s = ""
avg3s = ""

name4s = ""
class4s = ""
major4s = ""
avg4s = ""


def open_windows(check1, check2, check3, check4, formats, schools):
    global displayLogo
    displayLogo = check1

    global displayOrder
    displayOrder = check2

    global displaySV
    displaySV = check3

    global displayJudges
    displayJudges = check4

    global meetFormat
    meetFormat = formats

    global competingSchools
    competingSchools = schools

    global aScreen
    aScreen = arenaScreen.Window()
    aScreen.show()
    global sScreen
    sScreen = scorekeeperScreen.Window()
    sScreen.show()


def close_windows():
    aScreen.close()
    sScreen.close()


def update_score(team, score):
    if team == 1:
        global meetScores1
        global scores1

        # send score to database for gymnast
        # send score to cumulative AA competition for gymnast
        if len(scores1) == 5:
            scores1 = drop_lowest(scores1, score)

            meetScores1 = 0
            for i in range(0, len(scores1)):
                meetScores1 += scores1[i]
        else:
            scores1.append(score)
            meetScores1 += score

        arenaScreen.Window.update_scoreLabel1(aScreen, str(meetScores1))
    if team == 2:
        global meetScores2
        global scores2

        if len(scores2) == 5:
            scores2 = drop_lowest(scores2, score)

            meetScores2 = 0
            for i in range(0, len(scores2)):
                meetScores2 += scores2[i]
        else:
            scores2.append(score)
            meetScores2 += score

        arenaScreen.Window.update_scoreLabel2(aScreen, str(meetScores2))
    if team == 3:
        global meetScores3
        global scores3

        if len(scores3) == 5:
            scores3 = drop_lowest(scores3, score)

            meetScores3 = 0
            for i in range(0, len(scores3)):
                meetScores3 += scores3[i]
        else:
            scores3.append(score)
            meetScores3 += score

        arenaScreen.Window.update_scoreLabel3(aScreen, str(meetScores3))
    if team == 4:
        global meetScores4
        global scores4

        if len(scores4) == 5:
            scores4 = drop_lowest(scores4, score)

            meetScores4 = 0
            for i in range(0, len(scores4)):
                meetScores4 += scores4[i]
        else:
            scores4.append(score)
            meetScores4 += score

        arenaScreen.Window.update_scoreLabel4(aScreen, str(meetScores4))


def update_gymnast1():
    global name1s, class1s, major1s, avg1s

    name1s = "90000"
    class1s = "9999"
    major1s = "9934"
    avg1s = "pppjsf"
    arenaScreen.Window.update_gymnast1(aScreen, name1s, class1s, major1s, avg1s)

def update_gymnast2():
    global name2s, class2s, major2s, avg2s
    name2s = "90000"
    class2s = "9999"
    major2s = "9934"
    avg2s = "pppjsf"
    arenaScreen.Window.update_gymnast2(aScreen, name2s, class2s, major2s, avg2s)

def update_gymnast3():
    global name3s, class3s, major3s, avg3s
    name3s = "90000"
    class3s = "9999"
    major3s = "9934"
    avg3s = "pppjsf"
    arenaScreen.Window.update_gymnast3(aScreen, name3s, class3s, major3s, avg3s)

def update_gymnast4():
    global name4s, class4s, major4s, avg4s
    name4s = "90000"
    class4s = "9999"
    major4s = "9934"
    avg4s = "pppjsf"
    arenaScreen.Window.update_gymnast4(aScreen, name4s, class4s, major4s, avg4s)


def drop_lowest(array, value):
    # find the lowest score in the array
    min_index = 0
    for i in range(1, len(array)):
        if array[i] < array[min_index]:
            min_index = i

    # check to see if new score is lower than the lowest score in the array
    if value > array[min_index]:
        array[min_index] = value  # if new score is greater, replace the lowest score with new score

    return array

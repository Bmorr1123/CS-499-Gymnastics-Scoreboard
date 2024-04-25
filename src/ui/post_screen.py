import pprint
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from data import MeetData
from db_interface import DBInterface
from models import Gymnast

# Hardcoded cus I have 15 minutes left
position_list = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th"]


class PostScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Post Meet Screen")

        self.data = MeetData.get_data()
        self.db_interface = DBInterface.get_interface()
        self.school_scores = self.compile_school_scores()
        self.gymnast_scores = self.compile_gymnast_scores()
        self.final_school_scores, self.final_gymnast_scores = self.sum_scores(self.school_scores, self.gymnast_scores)

        # create a QHBoxLayout instance (for side-by-side placements)
        placements = QGridLayout()
        placements.setRowStretch(1, 1)

        # create a QVBoxLayout instance for each type of placement (final and all-around)
        finalScores = QVBoxLayout()
        finalScores.setContentsMargins(60, 0, 0, 0)
        aroundScores = QVBoxLayout()
        aroundScores.setContentsMargins(60, 0, 0, 0)

        # create score titles
        finalTitle = QLabel("Final Team Placements")
        finalTitle.setFont(QFont('Arial', 50))
        finalTitle.setAlignment(Qt.AlignCenter)
        aroundTitle = QLabel("All-Around Placements")
        aroundTitle.setFont(QFont('Arial', 50))
        aroundTitle.setAlignment(Qt.AlignCenter)

        for i, (school_name, score) in enumerate(self.final_school_scores):
            finalScore1 = QLabel(f"{position_list[i]} - Team Name: {school_name} \nScore: {score:.03f}")
            finalScore1.setFont(QFont('Arial', 32))
            finalScores.addWidget(finalScore1)

        for i, (gymnast_name, score, gymnast_id) in enumerate(self.final_gymnast_scores):
            aroundScore1 = QLabel(f"{position_list[i]}: {gymnast_name} {score}")
            aroundScore1.setFont(QFont('Arial', 32))
            aroundScores.addWidget(aroundScore1)

        # add titles to outer layout
        placements.addWidget(finalTitle, 0, 0)
        placements.addWidget(aroundTitle, 0, 1)

        # add score layouts to placements format layout
        placements.addLayout(finalScores, 1, 0)
        placements.addLayout(aroundScores, 1, 1)

        # set the layout on the application's window
        self.setLayout(placements)

    def compile_school_scores(self):
        event_lineup_managers = self.data.event_lineup_managers
        school_scores = {}
        # scores
        for i, elm in enumerate(event_lineup_managers):
            if elm is None:
                continue

            apparatus_scores = {}
            for lineup in elm.lineup_objects:
                lineup_entries = self.db_interface.get_lineup_entries_from_lineup(lineup)

                scores = [lineup_entry.score for lineup_entry in lineup_entries]
                apparatus_scores[lineup.apparatus_name] = scores

            pprint.pprint(apparatus_scores)
            school_scores[self.data.schools[i]] = apparatus_scores
        print("-------- TOTAL --------")
        pprint.pprint(school_scores)
        return school_scores

    def compile_gymnast_scores(self):
        event_lineup_managers = self.data.event_lineup_managers
        gymnast_scores = {}
        # scores
        for i, elm in enumerate(event_lineup_managers):
            if elm is None:
                continue
            for lineup in elm.lineup_objects:
                lineup_entries = self.db_interface.get_lineup_entries_from_lineup(lineup)
                for lineup_entry in lineup_entries:
                    if lineup_entry.gymnast_id not in gymnast_scores:
                        gymnast: Gymnast = self.db_interface.get_gymnast_by_id(lineup_entry.gymnast_id)[0]
                        gymnast_scores[gymnast.gymnast_id] = {
                            "full_name": f"{gymnast.first_name} {gymnast.last_name}",
                            "scores": []
                        }
                    gymnast_scores[lineup_entry.gymnast_id]["scores"].append(lineup_entry.score)

        print("--------- Gymnast Scores --------")
        pprint.pprint(gymnast_scores)

        return gymnast_scores

    def sum_scores(self, school_scores, gymnast_scores):
        school_sums = []
        for school_name, school in school_scores.items():
            apparatus_sums = []
            for apparatus, scores in school.items():
                scores.sort()
                apparatus_sums.append(sum(scores[:-1]))
            school_sums.append((school_name, sum(apparatus_sums)))

        gymnast_sums = []
        for gymnast_id, gymnast in gymnast_scores.items():
            full_name = gymnast["full_name"]
            scores = gymnast["scores"]

            if len(scores) == 4:
                gymnast_sums.append((full_name, sum(scores), gymnast_id))

        school_sums.sort(key=lambda school: school[1], reverse=True)
        gymnast_sums.sort(key=lambda gymnast: gymnast[1], reverse=True)

        pprint.pp(school_sums)
        pprint.pp(gymnast_sums)

        return school_sums, gymnast_sums


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PostScreen()
    window.show()
    sys.exit(app.exec_())

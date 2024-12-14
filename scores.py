import csv
from PyQt6 import QtWidgets
from StudentScores import Ui_Scores

class ScoresAll(QtWidgets.QMainWindow, Ui_Scores):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.submit_button.clicked.connect(self.submit_data)
        self.attempts_Input.textChanged.connect(self.update_attempts)
        self.data = []

    def update_attempts(self):
        try:
            attempts = int(self.attempts_Input.text())
            if attempts > 4:
                raise ValueError("Number of attempts cannot be greater than 4")
            self.label_firstattempt.setEnabled(attempts >= 1)
            self.first_input.setEnabled(attempts >= 1)
            self.label_secattempt.setEnabled(attempts >= 2)
            self.second_input.setEnabled(attempts >= 2)
            self.label_thirdattempt.setEnabled(attempts >= 3)
            self.third_input.setEnabled(attempts >= 3)
            self.label_forthattempts.setEnabled(attempts >= 4)
            self.forth_input.setEnabled(attempts >= 4)
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, 'Error', str(e))
            self.attempts_Input.setText('')
            return

    def validate_score(self, score: int):
        if 0 <= score <= 100:
            return True
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Score must be between 0 and 100')
            return False

    def submit_data(self):
        name = self.name_Input.text()
        student_id = self.id_Input.text()
        attempts = int(self.attempts_Input.text())
        scores = []

        if student_id in [entry['ID'] for entry in self.data]:
            QtWidgets.QMessageBox.warning(self, 'Error', 'ID already exists!')
            return

        if attempts >= 1:
            score = int(self.first_input.text())
            if self.validate_score(score):
                scores.append(score)
            else:
                return
        if attempts >= 2:
            score = int(self.second_input.text())
            if self.validate_score(score):
                scores.append(score)
            else:
                return
        if attempts >= 3:
            score = int(self.third_input.text())
            if self.validate_score(score):
                scores.append(score)
            else:
                return
        if attempts >= 4:
            score = int(self.forth_input.text())
            if self.validate_score(score):
                scores.append(score)
            else:
                return

        highest_score = max(scores) if scores else 0

        self.data.append({
            'Name': name,
            'ID': student_id,
            'Attempts': attempts,
            'Scores': scores,
            'Kept Score': highest_score
        })

        self.export_to_csv()

    def export_to_csv(self):
        with open('student_scores.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'ID', 'Attempts', 'Scores', 'Kept Score'])
            for entry in self.data:
                writer.writerow([entry['Name'], entry['ID'], entry['Attempts'], ','.join(map(str, entry['Scores'])), entry['Kept Score']])
        QtWidgets.QMessageBox.information(self, 'Success', 'Data exported to student_scores.csv')
        self.reset_window()

    def reset_window(self):
        self.name_Input.setText('')
        self.id_Input.setText('')
        self.attempts_Input.setText('')
        self.first_input.setText('')
        self.second_input.setText('')
        self.third_input.setText('')
        self.forth_input.setText('')
        self.label_firstattempt.setEnabled(False)
        self.first_input.setEnabled(False)
        self.label_secattempt.setEnabled(False)
        self.second_input.setEnabled(False)
        self.label_thirdattempt.setEnabled(False)
        self.third_input.setEnabled(False)
        self.label_forthattempts.setEnabled(False)
        self.forth_input.setEnabled(False)

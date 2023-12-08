"""
Graphical User Interface for the Grade Calculator application.
"""

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import sys
from grades import get_grades, write_grades_to_csv


class GradeCalculatorGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grade Calculator")
        self.setGeometry(100, 100, 400, 200)

        main_layout = QVBoxLayout()

        self.label_num_students = QLabel("Enter the number of students:")
        self.num_students_input = QLineEdit()

        self.label_scores = QLabel("Enter scores (separated by space):")
        self.scores_input = QLineEdit()

        self.submit_button = QPushButton("Submit")
        self.exit_button = QPushButton("Exit")

        main_layout.addWidget(self.label_num_students)
        main_layout.addWidget(self.num_students_input)
        main_layout.addWidget(self.label_scores)
        main_layout.addWidget(self.scores_input)
        main_layout.addWidget(self.submit_button)
        main_layout.addWidget(self.exit_button)

        self.submit_button.clicked.connect(self.calculate_grades)
        self.exit_button.clicked.connect(self.close)

        self.setLayout(main_layout)

    def calculate_grades(self) -> None:
        """
        Calculate grades based on user input and display the results.

        Raises:
            ValueError: If the number of students is not a positive integer,
                        if any score is negative,
                        or if the number of entered scores does not match the specified number of students.
        """
        try:
            num_students = int(self.num_students_input.text())
            if num_students <= 0:
                raise ValueError("Number of students must be a positive integer.")

            scores_input = self.scores_input.text()
            student_scores = [int(score) for score in scores_input.split()]

            if any(score < 0 for score in student_scores):
                raise ValueError("Scores cannot be negative.")

            if len(student_scores) != num_students:
                raise ValueError(f"Please enter exactly {num_students} score(s).")

            # Calculate grades using your get_grades function
            grades = get_grades(student_scores)

            # Display the grades (you can customize this part)
            grade_message = "\n".join(f"Student {i} score is {score}, and grade is {grade}." for i, (score, grade) in
                                      enumerate(zip(student_scores, grades), start=1))
            QMessageBox.information(self, 'Grades', grade_message)

            # Write results to CSV
            write_grades_to_csv(student_scores, grades)

            QMessageBox.information(self, 'Success', 'Results written to CSV.')
        except ValueError as e:
            QMessageBox.warning(self, 'Error', str(e))

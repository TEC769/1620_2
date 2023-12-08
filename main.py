"""
main.py - Main script to run the grade app.

This script initializes the PyQt application, creates an instance of the GradeCalculatorGUI class,
and runs the main event loop to display the grade GUI.
"""

from grades_gui import *


def main():
    app = QApplication(sys.argv)
    gui = GradeCalculatorGUI()
    gui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

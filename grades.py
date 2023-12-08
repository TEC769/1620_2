import csv
from typing import List


def get_grades(scores: List[int]) -> List[str]:
    """
    Assign grades based on a list of scores.

    Args:
        scores (List[int]): List of student scores.

    Returns:
        List[str]: List of grades corresponding to the input scores.
    """
    best = max(scores)
    grades = []

    for score in scores:
        if score >= best - 10:
            grades.append('A')
        elif score >= best - 20:
            grades.append('B')
        elif score >= best - 30:
            grades.append('C')
        elif score >= best - 40:
            grades.append('D')
        else:
            grades.append('F')

    return grades


def write_grades_to_csv(scores: List[int], grades: List[str]) -> None:
    """
    Write student scores and grades to a CSV file.

    Args:
        scores (List[int]): List of student scores.
        grades (List[str]): List of grades corresponding to the input scores.
    """
    filename = 'grades.csv'
    fieldnames = ['Student', 'Score', 'Grade']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, (score, grade) in enumerate(zip(scores, grades), start=1):
            writer.writerow({'Student': i, 'Score': score, 'Grade': grade})

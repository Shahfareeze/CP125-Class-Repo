# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:
import csv

def calculate_final_grades(input_file, output_file):
    """
    Calculate final grades from midterm and final scores.

    Args:
        input_file: path to scores CSV (student_id,midterm,final)
        output_file: path to output CSV file

    Returns:
        float: average of all final grades
    """
    # TODO: Implement this function
    f1= open (input_file, "r", newline="")
    f2= open (output_file, "w", newline="")

    scores = csv.reader(f1)
    output = csv.writer(f2)

    next(scores)
    result = []
    score = []
    for element in scores:
        final_grade = ((float(element[1]) * 0.4) + (float(element[2]) * 0.6))
        score.append(final_grade)
        result.append([element[0], f"{final_grade:.2f}"])

    output.writerow(["student_id", "final_grade"])
    output.writerows(result)

    f1.close()
    f2.close()

    return (sum(score)/len(score))

# Test your code here
result = calculate_final_grades("labs/lab08/exercise4/data/scores.csv", "labs/lab08/exercise4/data/grades.csv")
print(f"Average final grade: {result:.2f}")

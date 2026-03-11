# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    """
    Filter students with passing scores (>= 80) and write to output file.

    Args:
        input_file: path to input file (student_id and score on alternating lines)
        output_file: path to output file

    Returns:
        int: count of passing students
    """
    # TODO: Implement this function
    f1 = open(input_file, "r")
    f2 = open(output_file, "w")

    scores = []
    student_id = []

    for id in f1:
        item = f1.readline().strip()
        scores.append(item)
        student_id.append(id.strip())

    passing = []

    for i in range(0, len(scores)):
        if int(scores[i]) >= 80:
            passing.append(f"{student_id[i]} {scores[i]}")
            f2.write(f"{student_id[i]} {scores[i]}\n")

    f1.close()
    f2.close()

    return len(passing)




# Test your code here
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")

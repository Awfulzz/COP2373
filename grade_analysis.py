import numpy as np


# Load exam scores from the CSV file into a numpy array
def load_grades(filename):
    data = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=(2, 3, 4))
    return data


# Print the first few rows of the dataset
def print_first_rows(data, num_rows=5):
    print("First few rows of exam data:")
    print(data[:num_rows])
    print()


# Calculate and print statistics for each exam
def print_exam_statistics(data):
    print("Statistics for each exam:")

    for i in range(data.shape[1]):
        exam_scores = data[:, i]

        print(f"Exam {i + 1}:")
        print(f"Mean: {np.mean(exam_scores):.2f}")
        print(f"Median: {np.median(exam_scores):.2f}")
        print(f"Standard Deviation: {np.std(exam_scores):.2f}")
        print(f"Minimum: {np.min(exam_scores):.2f}")
        print(f"Maximum: {np.max(exam_scores):.2f}")
        print()


# Calculate and print overall statistics for all exams combined
def print_overall_statistics(data):
    all_scores = data.flatten()

    print("Overall statistics for all exams combined:")
    print(f"Mean: {np.mean(all_scores):.2f}")
    print(f"Median: {np.median(all_scores):.2f}")
    print(f"Standard Deviation: {np.std(all_scores):.2f}")
    print(f"Minimum: {np.min(all_scores):.2f}")
    print(f"Maximum: {np.max(all_scores):.2f}")
    print()


# Determine and print number of students who passed and failed each exam
def print_pass_fail_counts(data):
    print("Pass/Fail counts for each exam:")

    for i in range(data.shape[1]):
        exam_scores = data[:, i]
        passed = np.sum(exam_scores >= 60)
        failed = np.sum(exam_scores < 60)

        print(f"Exam {i + 1}:")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print()


# Calculate and print overall pass percentage across all exams
def print_overall_pass_percentage(data):
    total_scores = data.size
    total_passed = np.sum(data >= 60)
    pass_percentage = (total_passed / total_scores) * 100

    print("Overall pass percentage across all exams:")
    print(f"{pass_percentage:.2f}%")
    print()


def main():
    filename = "grades.csv"

    grades_data = load_grades(filename)

    print_first_rows(grades_data)
    print_exam_statistics(grades_data)
    print_overall_statistics(grades_data)
    print_pass_fail_counts(grades_data)
    print_overall_pass_percentage(grades_data)


if __name__ == "__main__":
    main()
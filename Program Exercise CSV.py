import csv

# Write student data to file
def write_grades():
    num_students = int(input('Enter number of students: '))

    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        # header
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        for i in range(num_students):
            print(f'\nStudent {i + 1}')

            first = input('First Name: ')
            last = input('Last Name: ')
            e1 = int(input('Exam 1: '))
            e2 = int(input('Exam 2: '))
            e3 = int(input('Exam 3: '))

            writer.writerow([first, last, e1, e2, e3])


# Read and display file
def read_grades():
    with open('grades.csv', 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            print('{:<15} {:<15} {:<10} {:<10} {:<10}'.format(
                row[0], row[1], row[2], row[3], row[4]
            ))


def main():
    write_grades()
    print()
    read_grades()


if __name__ == '__main__':
    main()
import csv


def get_top_performers(filepath, number_of_top_students):
    """A function which receives file path and returns names of top performer students"""
    students_list = list()
    student_list = list()
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if (row[0] != '') & (row[2] != ''):
                student_list.append(row[0])
                student_list.append(float(row[2]))
                students_list.append(tuple(student_list))
                student_list.clear()
    students_list.sort(key=lambda x: x[1])
    students_list.reverse()
    for item in students_list:
        student_list.append(item[0])
    return student_list[:number_of_top_students]


def write_to_csv_file(from_filepath, to_filepath):
    """A function which receives the file path with students info and writes CSV student
    information to the new file in descending order of age."""
    students_list = list()
    student_list = list()
    with open(from_filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if (row[0] != '') & (row[2] != ''):
                student_list.append(row[0])
                student_list.append(int(row[1]))
                student_list.append(float(row[2]))
                students_list.append(tuple(student_list))
                student_list.clear()
    students_list.sort(key=lambda x: x[1])
    with open(to_filepath, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(['student name', 'age', 'average mark'])
        for item in students_list:
            csv_writer.writerow(item)


def main():
    """Testing functions"""
    print(get_top_performers('data/students.csv', 5))
    write_to_csv_file('data/students.csv', 'data/reverse_age_students.csv')


if __name__ == '__main__':
    main()

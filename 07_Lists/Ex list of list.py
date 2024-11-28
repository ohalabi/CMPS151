def load_data(file_name):
    """Load the file into a two-dimensional list."""
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            name = parts[0]
            enrollment_date = parts[1]
            #The purpose of this line is to extract the grades from the line, 
            # convert them from strings to integers, and store them as a list of integers in the variable grades.
            grades = [int(grade) for grade in parts[2:]]  # Convert grades to integers manually
            data.append([name, enrollment_date, grades])
    return data

def calculate_student_averages(student_data):
    """Calculate and print the average grade for each student."""
    for student in student_data:
        name = student[0]
        grades = student[2]
        average = sum(grades) / len(grades)
        print(f"{name}'s average grade: {average:.2f}")

def find_highest_math_grade(student_data):
    """Find and return the name of the student with the highest Math grade."""
    highest_math_grade = 0
    top_student = ""
    for student in student_data:
        name = student[0]
        math_grade = student[2][0]  # Math is the first grade in the list
        if math_grade > highest_math_grade:
            highest_math_grade = math_grade
            top_student = name
    print(f"Student with the highest Math grade: {top_student} ({highest_math_grade})")

def count_students_by_year(student_data, year):
    """Count and print the number of students enrolled in the given year."""
    enrolled_in_year = 0
    for student in student_data:
        enrollment_date = student[1]
        year_of_enrollment = enrollment_date.split('-')[2]
        if year_of_enrollment == str(year):
            enrolled_in_year += 1
    print(f"Number of students enrolled in {year}: {enrolled_in_year}")

def main():
    file_name = "./07_Lists/students.txt"  # File containing the data
    year = 2022  # Year to filter by

    # Load the data
    student_data = load_data(file_name)
    
    # Process the data
    calculate_student_averages(student_data)
    find_highest_math_grade(student_data)
    count_students_by_year(student_data, year)

if __name__ == "__main__":
    main()
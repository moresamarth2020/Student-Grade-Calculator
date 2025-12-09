def grade_calculator():
    print("----- Student Grade Calculator -----\n")

    subjects = int(input("Enter number of subjects: "))
    marks = []

    for i in range(subjects):
        score = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(score)

    total = sum(marks)
    percentage = (total / (subjects * 100)) * 100

    # Grade logic
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F (Fail)"

    print("\n----- Result -----")
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

grade_calculator()

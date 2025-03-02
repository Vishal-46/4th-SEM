# Anna University GPA Calculator

# Grade to GPA Mapping
grade_map = {
    "O": 10,  # 90-100
    "A+": 9,  # 80-89
    "A": 8,   # 70-79
    "B+": 7,  # 60-69
    "B": 6,   # 50-59
    "C": 5,   # 40-49
    "F": 0    # <40 Fail
}

# Get number of subjects
num_subjects = int(input("Enter the number of subjects: "))

total_credits = 0
total_points = 0

# Loop through each subject
for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    credits = int(input(f"Enter credits for Subject {i}: "))

    # Determine grade
    if marks >= 90:
        grade = "O"
    elif marks >= 80:
        grade = "A+"
    elif marks >= 70:
        grade = "A"
    elif marks >= 60:
        grade = "B+"
    elif marks >= 50:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "F"
    grade_points = grade_map[grade]
    total_points += grade_points * credits
    total_credits += credits

    print(f"📌 Subject {i}: {marks} Marks → {grade} Grade → {grade_points} Points")
if total_credits == 0:
    print("\n❌ No valid subjects entered!")
else:
    gpa = total_points / total_credits
    print(f"\n🎓 Your GPA: {round(gpa, 2)} / 10")

5
# Tuples
student = ("Dhruvika", 6, "Primary", 11)
print(f"Student Profile: {student}")

# Tuple Operations
student_name = student[0]
print(f"\nStudent Name: {student_name}")

student_grade = student[1]
print(f"Student Grade: {student_grade}")

student_section = student[2]
print(f"Student Section: {student_section}")

student_subjects = student[3]
print(f"Student Subjects: {student_subjects}")

print(f"Student's First Two Details: {student[0:2]}")

# Sets
monday_subjects = {"English Language", "Social Studies", "Integrated Science", "Chinese"}
print(f"\nMonday Subjects: {monday_subjects}")

tuesday_subjects = {"Mathematics", "ICT", "Swimming", "Integrated Science", "Library"}
print(f"Tuesday Subjects: {tuesday_subjects}")

# Set Operations (1)
monday_subjects.add("Technology Studies")
print(f"\nUpdated Monday Subjects: {monday_subjects}")

tuesday_subjects.discard("Swimming")
print(f"Updated Tuesday Subjects: {tuesday_subjects}")

# Set Operations (2)
all_subjects = monday_subjects.union(tuesday_subjects)
print(f"\nAll Subjects of Both Days: {all_subjects}")

common_subjects = monday_subjects.intersection(tuesday_subjects)
print(f"Common Subjects of Both Days: {common_subjects}")

monday_subjects_only = monday_subjects.difference(tuesday_subjects)
print(f"Monday Subjects Only: {monday_subjects_only}")

tuesday_subjects_only = tuesday_subjects.difference(monday_subjects)
print(f"Tuesday Subjects Only: {tuesday_subjects_only}")

unique_subjects = monday_subjects.symmetric_difference(tuesday_subjects)
print(f"Unique Subjects: {unique_subjects}\n")

# Summary
print("-" * 135)
print("SCHOOL SUBJECT PLANNER SUMMARY")
print("-" * 135)
print(f"Student Name: {student_name}")
print(f"Student Grade: {student_grade}")
print(f"Monday Subjects: {monday_subjects}")
print(f"Tuesday Subjects: {tuesday_subjects}")
print(f"Common Subjects of Both Days: {common_subjects}")
print(f"Unique Subjects of Both Days: {unique_subjects}")
print("-" * 135)
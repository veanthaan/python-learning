students = []

while True:
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    students.append((name, marks, grade))

    choice = input("Add another student? (y/n): ")
    if choice.lower() != 'y':
        break

print("\n--- All Results ---")
for s in students:
    print("Name:", s[0], "| Marks:", s[1], "| Grade:", s[2])
# app.py - Student Management System

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"

def test_calculate_grade():
    s1 = Student(101, "Arihant", 85)
    assert s1.calculate_grade() == "B"
    print("Unit Test Passed: Grade calculation logic is correct!")

if __name__ == "__main__":
    print("=== STUDENT MANAGEMENT SYSTEM ===")
    test_calculate_grade()
    
    # Sample student records
    students = [
        Student(1, "Alice", 92),
        Student(2, "Bob", 78),
        Student(3, "Charlie", 45)
    ]
    
    print("\nStudent Records:")
    print("-" * 35)
    for s in students:
        print(f"ID: {s.roll_no} | Name: {s.name:<8} | Marks: {s.marks} | Grade: {s.calculate_grade()}")
    print("-" * 35)
    print("Application executed successfully inside Docker container!")
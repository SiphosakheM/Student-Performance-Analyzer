import json
import csv
from analyzer import Analyzer

class StudentPerformance:
    def __init__(self,name, surname , marks):
        self.names = name
        self.surnames = surname
        self.marks = marks
        
    def dictionary(self):
        return {"firstname": self.names, "lastname": self.surnames, "marks": self.marks }
    
    def to_list(self):
        return [self.names, self.surnames, self.marks]
    
def save_students(students):
    with open("class_register.json", "w") as j_file:
        json.dump([student.dictionary() for student in students], j_file, indent=4)
        
    with open("class_list.csv", "w") as c_file:
        write = csv.writer(c_file)
        write.writerow(["firstname", "lastname", "marks"])
        write.writerows([student.to_list() for student in students])
        
def load_from_json():
    try:
        with open("class_register.json", "r") as file:
            data = json.load(file)
            return [StudentPerformance(d["firstname"], d["lastname"], d["marks"]) for d in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def main():
    students = load_from_json()
    while True:
        print("\n------------ STUDENT PERFORMANCE MENU -------------")
        print("1. Add student  2. View Students  3. Show statistics 4.Save & Exit",sep= "\n")
        try:
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter first name: ").strip().title()
                surname = input("Enter surname: ").strip().title()

                try:
                    marks = float(input("Enter marks: "))
                except ValueError:
                    print("Invalid marks. Try again.")
                    continue

                student = StudentPerformance(name, surname, marks)
                students.append(student)
                
                save_students(students)
                print("Student added successfully.")
                
            elif choice == "2":
                if not students:
                    print("No students available.")
                else:
                    print("\n+----+------------+------------+-------+--------+")
                    print("| No | First Name | Last Name  | Marks | Status |")
                    print("+----+------------+------------+-------+--------+")

                    for key, student in enumerate(students, start=1):
                        status = "Pass" if student.marks >= 50 else "Fail"
                        print(f"| {key:<2} | {student.names:<10} | {student.surnames:<10} | {student.marks:<5} | {status:<6} |")

                    print("+----+------------+------------+-------+--------+")
                    
            elif choice == "3":
                if not students:
                    print("No data to analyze.")
                    continue

                analyzer = Analyzer(students)

                total = analyzer.total_students()
                average = analyzer.average_marks()
                highest = analyzer.highest_marks()
                lowest = analyzer.lowest_marks()
                ranked = analyzer.ranked_students()

                print("\n------------ Class Statistics -------------")
                print(f"Total Students: {total}")
                print(f"Average Marks: {average:.2f}")
                print(f"Highest Marks: {highest}")
                print(f"Lowest Marks: {lowest}")

                print("\n+------+------------+------------+-------+--------+")
                print("| Rank | First Name | Last Name  | Marks | Status |")
                print("+------+------------+------------+-------+--------+")

                for key, student in enumerate(ranked, start=1):
                    status = "Pass" if student.marks >= 50 else "Fail"
                    print(f"| {key:<4} | {student.names:<10} | {student.surnames:<10} | {student.marks:<5} | {status:<6} |")

                print("+------+------------+------------+-------+--------+")

            elif choice == "4":
                save_students(students)
                print("Data saved. Goodbye!")
                break

            else:
                print("Invalid option. Try again.")

        except ValueError:
            print("Enter a valid choice number")
            
main()
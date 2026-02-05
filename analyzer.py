class Analyzer:
    def __init__(self,students):
        self.students = students
        
    def total_students(self):
        return len(self.students)
    
    def average_marks(self):
        if not self.students:
            return 0
        return sum(student.marks for student in self.students) / len(self.students)
    
    def highest_marks(self):
        if not self.students:
            return 0
        return max(student.marks for student in self.students)
    
    def lowest_marks(self):
        if not self.students:
            return 0
        return min(student.marks for student in self.students)
    
    def ranked_students(self):
        return sorted(self.students, key=lambda x: x.marks, reverse=True)
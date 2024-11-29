class ClassRoom:
    def __init__(self,name) -> None:
        self.name = name
        self.subjects = []
        self.students = []
    
    def add_student(self,student):
        roll_no = f"{self.name}-{len(self.students)+1}"
        student.id = roll_no
        self.students.append(student)
    
    def add_subject(self,subject):
        self.subjects.append(subject)
    
    def take_semester_final_exam(self):
        for subject in self.subjects:
            subject.exam(self.students)
            
        result = []
        
        for student in self.students:
            final_grade_info = student.final_grade() 
            result.append(final_grade_info)
        return result
class Student:
    def __init__(self,name,cur_class,id):
        self.name = name
        self.cur_class = cur_class
        self.id = id
        
    def __repr__(self) -> str:
        return f'Student: {self.name}, class: {self.cur_class}, id: {self.id}'
    
    
class Teacher:
    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.id = id
    
    def __repr__(self) -> str:
        return f'Teacher: {self.name}, Subject: {self.subject}, Id: {self.id}'
    
   
class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teacher(self,name,subject):
        id = len(self.teachers)+1
        teacher = Teacher(name,subject,id)
        self.teachers.append(teacher)
        
    def enroll(self,name,fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            id = len(self.students)+1
            student = Student(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee-6500}'
        
    def __repr__(self) -> str:
        print('Welcome to', self.name)
        print('---------Our Teachers---------')
        for teacher in self.teachers:
            print(teacher)
        print(f'--------Our Students---------')
        for student in self.students:
            print(student)
        return f'All done for now'
        
        
# sakib = Student('Sakib',9,1)
# rakib = Teacher('Rakib','Algorithm',101)
# print(sakib)
# print(rakib)

phitron = School('Phitron')
phitron.enroll('alia',5200)
phitron.enroll('akib',8000)
phitron.enroll('sakib',90000)
phitron.enroll('salia',7000)

phitron.add_teacher('Tom Cruise','Algorithm')
phitron.add_teacher('Decap','Python')
phitron.add_teacher('Tourist','DS')

print(phitron)




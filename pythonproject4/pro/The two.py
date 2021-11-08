class Student(object):
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
    def study(self):
        print("%s在学习%s" % (self.name, self.subject))
student = Student("小明",20,"语文")
student.study()
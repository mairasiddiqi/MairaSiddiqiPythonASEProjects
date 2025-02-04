class Student:

    def __init__(self, name, age, average):
        self.name = name
        self.age = age
        self.average = average

    def __str__(self):
        return "Student: " + str(self.name) + ", Age: " + str(self.age) + ", Average: " + str(self.average)


class ClassRecord:

    def __init__(self):
        self.record = []
        self.index = 0

# add_student(self, student): Adds a Student object to the record if there is space; otherwise, prints "Record is full".
    def add_student(self, student):
        if self.index < 10:
            self.record.append(student)
            self.index += 1
        else:
            print("Record is full")

#print_record(self): Prints all students in the record.
    def print_record(self):
        for student in self.record:
            print(student)

#get_oldest_student(self): Returns the oldest student in the
    def get_oldest_student(self):
        oldest = self.record[0]
        for student in self.record:
            if student.age > oldest.age:
                oldest = student
        return oldest

#get_class_average(self): Returns the average grade of all students in the record.
    def get_class_average(self):
        total = 0
        for average in self.record:
            total += average
        return total / len(self.record)

#get_highest_average_grade(self): Returns the student with the highest average grade.
    def get_highest_average_grade(self):
        highest = 0
        for average in self.record:
            if average > highest:
                highest = average
        return highest

# get_student_ages(self): Returns a list of ages of all students.
    def get_student_ages(self):
        ages = []
        for student in self.record:
            ages.append(student.age)
        return ages

#get_passing_students(self): Returns a list of names of students with an average grade of 50 or higher.
    def get_passing_students(self):
        passing = []
        for student in self.record:
            if student.average >= 50:
                passing.append(student.name)
        return passing

#pass_fail_remarks(self): Returns a list of passes ('P') or fail ('F') based on student averages.
    def pass_fail_remarks(self):
        remarks = []
        for student in self.record:
            if student.average >= 50:
                remarks.append('P')
            else:
                remarks.append('F')
        return remarks

#print_by_age(self, age): Prints the names of students who are at least the specified age
    def print_by_age(self, age):
        for student in self.record:
            if student.age >= age:
                print(student.name)

#search_student(self, name): Returns the student with the given name.
    def search_student(self, name):
        for student in self.record:
            if student.name == name:
                return student
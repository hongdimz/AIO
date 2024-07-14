# câu 1
import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / torch.sum(exp_x, dim=0, keepdim=True)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdim=True)
        return x_exp / partition

# câu 2
# a: tạo class student, teacher, doctor


class Student():
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print('Student')
        print(f'Name: {self.name}')
        print(f'Year of birth: {self.yob}')
        print(f'Grade: {self.grade}')


class Teacher():
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print('Teacher')
        print(f'Name: {self.name}')
        print(f'Year of birth: {self.yob}')
        print(f'Grade: {self.subject}')


class Doctor():
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print('Doctor')
        print(f'Name: {self.name}')
        print(f'Year of birth: {self.yob}')
        print(f'Grade: {self.specialist}')

# b tạo class ward


class Ward():
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def describe(self):
        for i in self.people:
            print('----')
            i.describe()
    # count doctor method

    def count_doctor(self):
        count = 0
        for i in self.people:
            if isinstance(i, Doctor) == True:
                count = count + 1
        return count
    # sort people theo năm sinh

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob)

    def compute_average(self):
        count = 0
        sum = 0
        for i in self.people:
            if isinstance(i, Teacher) == True:
                count = count + 1
                sum = sum + i.yob
        return sum/count


student1 = Student(name=" studentA ", yob=2010, grade="7")
# student1 . describe ()
teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
# teacher1 . describe ()
doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
# doctor1 . describe ()
teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
ward1 = Ward(name=" Ward1 ")
ward1. add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
# ward1.describe ()
# print(f'Number of doctor: {ward1.count_doctor()}')
# ward1.sort_age ()
# ward1.describe ()
# print ( f"\Average year of birth ( teachers ): { ward1 . compute_average ()}")

# câu 3 STACK


class MyStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.lst = []

    def is_empty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.lst) == self.capacity:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty() == True:
            print('List rỗng, không thể xóa')
        else:
            return self.lst.pop()

    def push(self, value):
        if self.is_full() == True:
            print('List đầy, không thể thêm')
        else:
            self.lst.append(value)

    def top(self):
        if self.is_empty() == True:
            print('List rỗng, không có top')
            return None
        else:
            return self.lst[-1]
# stack1 = MyStack(capacity =5)
# stack1.push(1)
# stack1.push (2)
# print (stack1.is_full())
# print ( stack1.top () )
# print ( stack1.pop () )
# print ( stack1.top () )
# print ( stack1.pop () )
# print ( stack1.is_empty () )

# câu 4 QUEUE


class MyQueue():
    def __init__(self, capacity):
        self.capacity = capacity
        self.lst = []

    def is_empty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self.lst) == self.capacity:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty() == True:
            print('List rỗng, không thể xóa')
        else:
            return self.lst.pop(0)

    def enqueue(self, value):
        if self.is_full() == True:
            print('List đầy, không thể thêm')
        else:
            self.lst.append(value)

    def front(self):
        if self.is_empty() == True:
            print('List rỗng, không có front')
            return None
        else:
            return self.lst[0]

# queue1 = MyQueue ( capacity =5)
# queue1 . enqueue (1)
# queue1 . enqueue (2)
# print ( queue1 . is_full () )
# print ( queue1 . front () )
# print ( queue1 . dequeue () )
# print ( queue1 . front () )
# print ( queue1 . dequeue () )
# print ( queue1 . is_empty () )

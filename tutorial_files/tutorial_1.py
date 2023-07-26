# Intro to classes

class Student:
    def __init__(self, first, last, major, dean_bucks):
        self.first = first
        self.last = last
        self.major = major
        self.email = first + '.' + last + "@greendale.edu"
        self.dean_bucks = dean_bucks

    # this is a method of the Student class
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_dean_bucks(self):
        self.dean_bucks = int(self.dean_bucks * 1.06)

# these are instances of the class
stu_1 = Student('Britta', 'Perry', 'Psychology', 50)
stu_2 = Student('Jeff', 'Winger', 'Independent Studies', 10000)
stu_3 = Student('Troy', 'Barnes', 'AC Repair', 700)
stu_4 = Student('Annie', 'Edison', 'Hospital Administration', 600)
stu_5 = Student('Abed', 'Nadir', 'Film Studies', 800)
stu_6 = Student('Shirley', 'Bennett', 'Business', 750)

# calls an attribute of an instance
print(stu_2.email)
print(stu_2.dean_bucks)

## These two do the same thing in diff ways
# calls function/method on instance
print(stu_2.fullname())
# calls method on the class, we must specify the instance
print(Student.fullname(stu_2))

print(stu_3.dean_bucks)
stu_3.apply_dean_bucks()
print(stu_3.dean_bucks)

print("Deenspursal Amount for All Students ", Student.deanspursal_amount)
# instances of the class access the variable via the class
print("Deenspursal Amount for", stu_1.fullname(), stu_1.deanspursal_amount)
print("Deenspursal Amount for", stu_2.fullname(), stu_2.deanspursal_amount)

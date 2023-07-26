# Class Variables apply to all instances of the class
class Student:
    
    num_of_students = 0
    
    # class variable added to the 'Student' class
    deanspursal_amount = 1.34
    
    def __init__(self, first, last, major, dean_bucks):
        self.first = first
        self.last = last
        self.major = major
        self.email = first + '.' + last + "@greendale.edu"
        self.dean_bucks = dean_bucks

        # under the init b/c init runs every time so..
        Student.num_of_students += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # access Class Variable via the Student Class
    def apply_raise(self):
        self.dean_bucks = int(self.dean_bucks * Student.deanspursal_amount)
    # Or, access the Class Variable via the instance of the Student Class
    # this is the better option b/c it lets us change the variable for diff. instances
    def apply_raise(self):
        self.dean_bucks = int(self.dean_bucks * self.deanspursal_amount)

# Our instances of the Student Class
stu_1 = Student('Britta', 'Perry', 'Psychology', 50)
stu_2 = Student('Jeff', 'Winger', 'Independent Studies', 100000)
stu_3 = Student('Troy', 'Barnes', 'AC Repair', 700)
stu_4 = Student('Annie', 'Edison', 'Hospital Administration', 600)
stu_5 = Student('Abed', 'Nadir', 'Film Studies', 800)
stu_6 = Student('Shirley', 'Bennett', 'Business', 750)


print(Student.num_of_students)

# # creates an attribute in the stu_2 instance 
# stu_2.deanspursal_amount = 2.34

# # demonstrates how the class variable is availible to the entire Student class
# print("Deenspursal Amount for All Students ", Student.deanspursal_amount)
# # instances of the class access the variable via the class
# print("Deenspursal Amount for", stu_1.fullname(), stu_1.deanspursal_amount)
# print("Deenspursal Amount for", stu_2.fullname(), stu_2.deanspursal_amount)


###
### prints namespaces so you can see their attribute lists
# # namespace of the class
# print(Student.__dict__)

# # namespace of the instance
#print(stu_2.__dict__)
# pass


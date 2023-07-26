# Regular Methods, Class Methods, and Static Methods
#################
# Regular methods automatically take the instance "self" as the 1st argument
# Class methods allow us to use the Class as the 1st argument instead
# 'cls' is a convention to represent class in a class method as "class" is a py keyword
# Static Methods don't pass anything automatically - they have a logical connection to the class

import datetime

class Student:
    
    num_of_students = 0
    deanspursal_amount = 1.34
    
    def __init__(self, first, last, major, dean_bucks):
        self.first = first
        self.last = last
        self.major = major
        self.email = first + '.' + last + "@greendale.edu"
        self.dean_bucks = dean_bucks

        Student.num_of_students += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.dean_bucks = int(self.dean_bucks * self.deanspursal_amount)

    # turns reg. method into "class method"
    @classmethod
    def set_deanspursal_amount(cls, amount):
        cls.deanspursal_amount = amount 


    # alt. constructor, creates new stu from hyphanated string
    @classmethod
    def from_string(cls, new_stu):
        first, last, major, dean_bucks = new_stu.split('-')
        return cls(first, last, major, dean_bucks)

    # returns if a particular day was a school day
    @staticmethod
    def is_schoolday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True




stu_1 = Student('Britta', 'Perry', 'Psychology', 50)
stu_2 = Student('Jeff', 'Winger', 'Independent Studies', 100000)
stu_3 = Student('Troy', 'Barnes', 'AC Repair', 700)
stu_4 = Student('Annie', 'Edison', 'Hospital Administration', 600)
stu_5 = Student('Abed', 'Nadir', 'Film Studies', 800)
stu_6 = Student('Shirley', 'Bennett', 'Business', 750)

# # use class method to globally change the amount for entire class
# Student.set_deanspursal_amount(3.56)

# # demonstrates how the class variable is availible to the entire Student class
# print("Deenspursal Amount for All Students ", Student.deanspursal_amount)
# # instances of the class access the variable via the class
# print("Deenspursal Amount for", stu_1.fullname(), stu_1.deanspursal_amount)
# print("Deenspursal Amount for", stu_2.fullname(), stu_2.deanspursal_amount)


# Create a new student from a string that has hyphenated values (depreciated by the alt. constructor)
new_stu_1 = 'Benjamin-Chang-Spanish-51'
new_stu_2 = 'Alex StarBurns-Osbourne-Chemistry-564'
new_stu_3 = 'Maginitude-Youngblood-Political Science-1232'

# # split is a py function to parse strings
# first, last, major, dean_bucks = new_stu_1.split('-')

stu_7 = Student.from_string(new_stu_1)

#print(stu_7.email)

my_date = datetime.date(2022, 7, 25)
print(Student.is_schoolday(my_date))



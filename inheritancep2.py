"""
sam goode
7/8/2020
sgoode@dmacc.edu
this code will display two employees one on salary and the other on hourly.
"""


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name: ' + self.name + '\nAge: ', self.age)


class SalariedEmployee(Employee):
    def __init__(self, name, age, start_date, salary):
        Employee.__init__(self, name, age)
        self.start_date = start_date
        self.salary = salary

    def give_raise(self, hike):
        self.salary += hike

    def display(self):
        Employee.display(self)
        print('Start date: ' + self.start_date + '\nSalary: ', self.salary)


class HourlyEmployee(Employee):
    def __init__(self, name, age, start_date, hourly_pay):
        Employee.__init__(self, name, age)
        self.hourly_pay = hourly_pay
        self.start_date = start_date

    def give_raise(self, hourly_raise):
        self.hourly_pay += hourly_raise

    def display(self):
        Employee.display(self)
        print('Start date: ' + self.start_date + '\nHourly pay: ', self.hourly_pay)


e1 = SalariedEmployee('sam', 26, '07/08/2020', 100000)
e1.display()
e2 = HourlyEmployee('other sam', 29, '07/08/2020', 35)
e2.display()

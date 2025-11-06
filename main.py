## main.py
import my_maths

result = my_maths.add(5,6)
print("Addition:",result)

print("PI value:" ,my_maths.PI)


# main.py

# Import base class from module
from base_module import Employee

# Child class
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_department(self):
        print(f"{self.name} manages the {self.department} department.")

    def approve_leave(self, emp_name, days):
        print(f"{self.name} approved {days} days leave for {emp_name}.")

# Create objects
emp = Employee("Ali", 50000)
emp.show_info()
emp.annual_salary()

mgr = Manager("Sana", 80000, "Finance")
mgr.show_info()
mgr.show_department()
mgr.approve_leave("Hamza", 3)



# main.py

from base_module import Student

obj = Student("Memoona", 22)
obj.show_name()
obj.display_age()

# Accessing protected variable directly (not recommended)
print(obj._age)  # ⚠️ Possible, but breaks encapsulation rules


# main.py

from base_module import Person

# Create object
p1 = Person("Memoona", 24, 50000)

# Access public variable
print("Public:", p1.name)
# Access protected variable (possible but not recommended)
print("Protected:", p1._age)

# Try accessing private variable (will give error if direct)
# print(p1.__salary)  # ❌ Uncommenting this will raise AttributeError

# Use class methods
p1.show_info()
p1._age_check()
p1.show_bonus()
p1.view_salary()
p1.update_salary(60000)
p1.view_salary()

# Using loop method
p1.work_days(10)

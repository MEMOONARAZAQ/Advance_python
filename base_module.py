# base_module.py

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: Rs.{self.salary}")

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name}'s salary increased to Rs.{self.salary}")

    def annual_salary(self):
        yearly = self.salary * 12
        print(f"{self.name}'s annual salary is Rs.{yearly}")
        return yearly


# base_module.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # Protected variable

    def show_name(self):
        print(f"Name: {self.name}")

# Derived class (can access protected variable)
class Student(Person):
    def display_age(self):
        print(f"Age: {self._age}")






# base_module.py

class Person:
    def __init__(self, name, age, salary):
        # Public variable
        self.name = name

        # Protected variable (can be accessed in subclasses)
        self._age = age

        # Private variable (only accessible within the class)
        self.__salary = salary

    # Public method
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Salary (protected): Hidden for privacy")

    # Protected method (meant for internal use)
    def _age_check(self):
        if self._age < 18:
            print(f"{self.name} is underage.")
        elif 18 <= self._age < 60:
            print(f"{self.name} is an adult.")
        else:
            print(f"{self.name} is a senior citizen.")

    # Private method to handle salary safely
    def __bonus_calculation(self):
        bonus = 0
        if self._age < 25:
            bonus = self.__salary * 0.10
        elif self._age <= 50:
            bonus = self.__salary * 0.20
        else:
            bonus = self.__salary * 0.15
        return bonus

    # Public method to safely access private variable
    def show_bonus(self):
        bonus = self.__bonus_calculation()
        print(f"Bonus for {self.name}: Rs.{bonus}")

    # Method with a loop (simulate working days)
    def work_days(self, total_days):
        print(f"\n{self.name}'s monthly record:")
        for day in range(1, total_days + 1):
            if day % 7 == 0:
                print(f"Day {day}: Sunday — Holiday 💤")
            else:
                print(f"Day {day}: Working ✅")

    # Method to safely update private variable
    def update_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print(f"{self.name}'s salary updated successfully!")
        else:
            print("❌ Invalid salary amount.")

    # Method to view private variable safely
    def view_salary(self):
        print(f"{self.name}'s current salary is Rs.{self.__salary}")

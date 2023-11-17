#!/usr/bin/env python3
class Person:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

persona1 = Person

    def display_info(self):
        print(f"This is {person1.first_name} {person1.last_name}, born on {person1.birthdate}")

    def get_full_name(self):
        return(f"This is {person1.first_name} {person1.last_name}, born on {person1.birthdate}")

class User(Person):
    def __init__(self, first_name, last_name, birthdate, username):
        super().__init__(first_name, last_name, birthdate)
        self.username = username
        self.__password = None

user1 = User

    def display_info(self):
        return super().display_info(f"This is {user1.first_name} {user1.last}, born on {user1.birthdate} with username: {user1.username}")

    def to_dictionary(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate":  self.birthdate,
            "username": self.username,
            "password": self._password
            }

    def __password(self):
        return(self.__password)
    
    def __password(self, new_password):
        pass

class Employee(Person):
    def __init__(self, first_name, last_name, birthdate, employee_id):
        super().__init__(first_name, last_name, birthdate)
        self.employee_id = employee_id

employ1 = Employee
    def display_info(self):
        return super().display_info(f"This is {employ1.first_name} {employ1.last_name}, born on {employ1.birthdate} with employee ID: {employ1.employee}")

    def to_dictionary(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate":  self.birthdate,
            "employee_id": self.employee_id
        }
    def get_employee_id(self):
        pass

persona1 = Person ("Juan", "Fernandez", "1995-05-05")
user1 = User ("Juan", "Fernandez", "1995-05-05", "Juan.Fernandez")
employ1 = Employee ("Juan", "Fernandez", "1995-05-05", "E54321")
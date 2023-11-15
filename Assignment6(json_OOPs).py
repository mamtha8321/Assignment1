# Assignment-1
# 1.A python program that reads this information from the JSON file and saves the information into a list of objects of Employee class. 
# Finally print the list of the Employee objects.


import json
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
employee_data={"employees":[
    {
        "Name": "Mahender",
      "DOB": "1990-05-15",
      "Height": 175,
      "City": "Hyderabad",
      "State": "Telangana"
    },
    {
      "Name": "Manju",
      "DOB": "1985-08-22",
      "Height": 160,
      "City": "Warangal",
      "State": "Telangana"
    },
    {
      "Name": "Mamatha",
      "DOB": "1992-03-10",
      "Height": 180,
      "City": "Ramagundam",
      "State": "Telangana"
    },
    {
      "Name": "Rajeshwari",
      "DOB": "1988-11-28",
      "Height": 165,
      "City": "Tirupathi",
      "State": "Andhra Pradesh"
    },
    {
      "Name": "Sathya Narayana",
      "DOB": "1995-07-03",
      "Height": 170,
      "City": "Bangalore",
      "State": "Karnataka"
    }
  ]
}


with open('employee.json', 'w') as file:
    json.dump(employee_data, file)

with open('employee.json') as file:
    data = json.load(file)
    employee_list = []

    for employee_data in data['employees']:
        name = employee_data['Name']
        dob = employee_data['DOB']
        height = employee_data['Height']
        city = employee_data['City']
        state = employee_data['State']
        employee = Employee(name, dob, height, city, state)
        employee_list.append(employee)

for employee in employee_list:
    print("Name:", employee.name)
    print("DOB:", employee.dob)
    print("Height:", employee.height)
    print("City:", employee.city)
    print("State:", employee.state)
    print()

# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.

import json
indian_states = {
    "Andhra Pradesh": "Amaravathi",
    "Telangana": "Hyderabad",
    "Karnataka": "Bengaluru",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Tamil Nadu": "Chennai",
    }
with open('states and capital.json', 'w') as file:
    json.dump(indian_states, file)

print("Indian states and capitals have been written to indian_states.json.")


# Assignment-2
#1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
#c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
#d. Create objects and implement the above functionalities.

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def get_info(self):
        print("Coat Color:", self.coat_color)

class JackRussellTerrier(Dog):
    def _init_(self, name, age, coat_color):
        super()._init_(name, age, coat_color)

    def fetch_ball(self):
        print(self.name, "is fetching the ball.")

    def bark(self):
        print(self.name, "is barking.")

class Bulldog(Dog):
    def _init_(self, name, age, coat_color):
        super()._init_(name, age, coat_color)

    def guard_house(self):
        print(self.name, "is guarding the house.")

    def jump(self):
        print(self.name, "is jumping.")

dog1 = Dog("Leo", 5, "Brown")
dog1.description()
dog1.get_info()
print()

dog2 = JackRussellTerrier("Bella", 6, "White")
dog2.description()
dog2.get_info()
dog2.fetch_ball()
dog2.bark()
print()

dog3 = Bulldog("Jigi", 4, "Black")
dog3.description()
dog3.get_info()
dog3.guard_house()
dog3.jump()
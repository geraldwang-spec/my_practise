import sys
import os
from datetime import datetime

class AgeSystem_adv:
    """a age system adv"""
    def __init__(self, name, age) -> None:
        self.name = name
        self.__age = age

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int):
        """set age"""
        if not (1 <= value <= 150):
            print(f"warning: age {value} is unreasonable. auto setting 0 ")
            self.__age = 0
        else:
            self.__age = value

    @property
    def get_100_year(self) -> int:
        return 100 - self.__age + datetime.now().year

    def __str__(self) -> str:
        return f"name :{self.name: <10} | age: {self.__age:<3} | 100 old of year: {self.get_100_year}"

    def __get_base_path(self) -> str:
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        else:
            return os.path.dirname(os.path.abspath(__file__))

    def save_to_file(self, filename="characters.txt"):
        try:
            base_path = self.__get_base_path()
            file_path = os.path.join(base_path,  filename)
            print(f"file_path = {file_path}")
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(f"Name: {self.name}, Age: {self.age}\n")
            print(f"Successfully saved {self.name} to {filename}")
        except IOError as e:
            print(f"Error saving to file: {e}")


def run_system():
    record = []
    while True:
        name = input("Give me your name (enter \"quit\" or \"q\" exit): ")
        print(f"Your name is {name}")

        if name.lower() == 'quit' or name.lower() == 'q':
            print("Goodbye!")
            break

        try:
            age_input = input('Give my your age (enter \"quit\" or \"q\" exit):')
            if age_input.lower() == 'quit' or name.lower() == "q":
                print("Goodbye!")
                break
            
            record.append(AgeSystem_adv(name, int(age_input)))
            print(f"Recorded: {name}")
        except ValueError:
            print("Error: Age must be a number. Please try again.")

    for i in record:
        print(i)

def run_system1():
    raw_data = [("User"+str(i), i %120) for i in range(1000000)]
    people_generator = (AgeSystem_adv(name, age) for name, age in raw_data)
    
    print(f"generator building")
    people_gen = sys.getsizeof(people_generator) / 1024
    print(f"people_gen size: {people_gen}")

    print("--get three --")
    for _ in range(3):
        person = next(people_generator)
        print(person)
        people_gen = sys.getsizeof(people_generator) / 1024
        print(f"3 people_gen size: {people_gen}")

def run_system2():
    record = []
    while True:
        name = input("Give me your name (enter \"quit\" or \"q\" exit): ")
        print(f"Your name is {name}")

        if name.lower() == 'quit' or name.lower() == 'q':
            print("Goodbye!")
            break

        try:
            age_input = input('Give my your age (enter \"quit\" or \"q\" exit):')
            if age_input.lower() == 'quit' or name.lower() == "q":
                print("Goodbye!")
                break
            
            record.append(AgeSystem_adv(name, int(age_input)))
            print(f"Recorded: {name}")
        except ValueError:
            print("Error: Age must be a number. Please try again.")

    for i in record:
        i.save_to_file()
        print(i)

def advance_character_input():
    print("advance character input")
    # run_system()
    # run_system1()
    run_system2()

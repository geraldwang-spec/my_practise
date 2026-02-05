from datetime import datetime, timezone
from typing import Self

def Character_Input():
    print("Character Input")
    while True:
        name = input("Give me your name: ")
        print(f"Your name is {name}")

        if name.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            age_input = input('Give my your age:')
            if age_input.lower() == 'quit':
                print("Goodbye!")
                break
            age = int(age_input)
            print(f"Your age is {age}")
            print(f"100 years old in {100 - age+ int(datetime.now().year)}")
        except ValueError:
            print("Error: Age must be a number. Please try again.")

class AgeSystem:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    @property
    def get_100_year(self):
        return 100 - self.age + int(datetime.now().year)

def Character_Input_System():
    record = []
    while True:
        name = input("Give me your name: ")
        print(f"Your name is {name}")

        if name.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            age_input = input('Give my your age:')
            if age_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            record.append(AgeSystem(name, int(age_input)))
            print(f"Recorded: {name}")
        except ValueError:
            print("Error: Age must be a number. Please try again.")

    for i in record:
        print(f"name: {record[i].name}")

def practice_ex():
    print("practice_ex")
    # Character_Input()
    Character_Input_System()

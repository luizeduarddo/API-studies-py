import datetime
import math
from typing import List

class Person:
    def __init__(
            self, 
            name: str, 
            lastname: str, 
            birth_date: datetime.date) -> None: 
        self.birth_date = birth_date
        self.lastname = lastname
        self.name = name
    
    @property
    def age(self) -> int:
        return math.floor((datetime.date.today() - self.birth_date).days / 365.2425)

    def __str__(self) -> str:
        return f"{self.name} {self.lastname} has {self.age} years"

class Curriculum:
    def __init__(self, person: Person, experiencies: List[str]):
        self.experiences = experiencies
        self.person = person
        
    @property
    def amount_experiences(self) -> int:
        return len(self.experiences)
    
    @property
    def current_company(self) -> str:
        return self.experiences[-1]
    
    def add_experiencies(self, experience: str) -> None:
        self.experiences.append(experience)
    
    def __str__(self):
        return  f"{self.person.name} {self.person.lastname} has {self.person.age} years and has " \
                f"worked on {self.amount_experiences} company and currently" \
                f"work at company {self.current_company}"
    


luiz = Person(name='Luiz', lastname='Lopes', birth_date=datetime.date(1996, 1, 11))

curriculum_luiz = Curriculum(
    person= luiz,
    experiencies=['CNPQ', 'UFC', 'SECFIN', 'ENGIMAGEM']
)

print(curriculum_luiz.person.age)
print(curriculum_luiz)
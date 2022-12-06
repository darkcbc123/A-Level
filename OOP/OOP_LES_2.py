class Employee:
    def __init__(self, name, day_sal, work_days) :
        self.name = name
        self.day_sal = day_sal
        self.work_days = work_days
       
        
    def work(self):
        return f"I come to the office."
    
    
    def __eq__(self, other):
        return self.day_sal == other.day_sal
    
    
    def __str__(self):
        return f"Посада: {self.name}"
    
    
    def check_salary(self):
        total_sum = self.work_days * self.day_sal
        return total_sum
            

class Recruiter(Employee):
    
    def work(self):
        return super().work()[:-1] + ' and start to hiring'



class Developer(Employee):
    def __init__(self, name, day_sal, work_days, tech_stack):
       super().__init__(name, day_sal, work_days)
       self.tech_stack = tech_stack
     
        
    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)
    
    def work(self):
        return super().work()[:-1] + ' and start to coding'   
    
    def __add__(self, other):
        tech_unique = []
        for i in self.tech_stack:
            if i not in other.tech_stack:
             tech_unique.append(i)
        if self.check_salary() > other.check_salary():
            biggest_salary = self.check_salary()
        else:
            biggest_salary = other.check_salary()
        return f"{self.name} {other.name}, {tech_unique}, {biggest_salary}" 
        
    
el1 = Developer('vlad', 15, 25, ['Go', 'Java', 'Kotlin', 'PHP', 'C#'])
el2 = Developer('danya', 20, 30, ['Go', 'Java', 'Kotlin'])

our = el1 + el2

print(our)


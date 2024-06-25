class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print(f"Welcome to the college {self.name}")
        
s1=student("Ali raza",88)
s1.welcome()
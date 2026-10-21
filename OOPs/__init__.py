class Details:
    def __init__(self, name, age):
        print("This is skiped")
        self.name = name
        self.age = age

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def info(self):
        print(f"name: {self.name} age:{self.age} gender: {self.gender}")


obj1 = Details("Leelavardhan", "23", "Male")
obj2 = Details("Ram","25")
obj1.info()
obj2.info()

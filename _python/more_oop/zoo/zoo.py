class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age  = age
        self.health = health
        self.happiness = happiness
    def display_info(self):
        print(self.name, self.health, self.happiness)
    def feed(self):
        self.health += 10
        self.happiness += 10
    def introduce(self):
        print('My name is {}. {} years old.'.format(self.name, self.age))

class Lion(Animal):
    def __init__(self, name, age, health, happiness, mane):
        super().__init__(name, age, health, happiness)
        self.mane = True
    def barking(self):
        self.happiness += 10
        self.health -= 5
    def introduce(self):
        super().introduce()
        print("I'm Lion. The king of animal!")

class Tiger(Animal):
    def __init__(self, name, age, health, happiness, nap_time):
        super().__init__(name, age, health, happiness)
        self.nap_time = nap_time
    def nap(self, hour):
        self.nap_time += hour
        if self.nap_time > 3:
            self.happiness += 5
            self.health += 5
            self.nap_time = 0
    def introduce(self):
        super().introduce()
        print("I'm Tiger. The bigger size of cat!")

class Bear(Animal):
    def __init__(self, name, age, health, happiness, strength):
        super().__init__(name, age, health, happiness)
        self.strength = strength    
    def eat_fish(self, fish):
        if fish == "salmon":
            self.happiness += 20
            self.health += 20
        else:
            self.health += 5
    def introduce(self):
        super().introduce()
        print("I'm Bear. I usually sleep whole winter..")

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name, age):
        self.animals.append( Lion(name, age, 50, 50, True) )
    def add_tiger(self, name, age):
        self.animals.append( Tiger(name, age, 50, 50, 0) )
    def add_bear(self, name, age):
        self.animals.append( Bear(name, age, 50, 50, 50) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
    def feed(self, animal_name):
        for animal in self.animals:
            if animal.name == animal_name:
                animal.feed()
    def feed_all(self):
        for animal in self.animals:
            print("{} said I'm full".format(animal.name))
            animal.feed()
    def introduce_all(self):
        for animal in self.animals:
            print("-"*30, animal.name, "-"*30)
            animal.introduce()
    def daily_activity(self):
        for animal in self.animals:
            if type(animal).__name__ == "Lion":
                animal.barking()
            if type(animal).__name__ == "Tiger":
                animal.nap(4)
            if type(animal).__name__ == "Bear":
                animal.eat_fish("salmon")

zoo1 = Zoo("My Zoo")
zoo1.add_lion("Nala", 5)
zoo1.add_lion("Simba", 3)
zoo1.add_tiger("Rajah", 8)
zoo1.add_tiger("Shere Khan", 1)
zoo1.add_bear("Poo", 9)
zoo1.feed("Nala")
zoo1.feed_all()
zoo1.daily_activity()
zoo1.print_all_info()
zoo1.introduce_all()
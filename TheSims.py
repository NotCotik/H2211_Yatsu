import random

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 12},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Lexus": {"fuel": 80, "strength": 120, "consumption": 14}
}

pet_list = {
    "Cat": {"price_food": 10, "joy": 15, "mess_power": 5},
    "Dog": {"price_food": 15, "joy": 25, "mess_power": 10},
    "Parrot": {"price_food": 5, "joy": 10, "mess_power": 3}
}


class Pet:
    def __init__(self, pet_dict):
        self.kind = random.choice(list(pet_dict))
        self.joy = pet_dict[self.kind]["joy"]
        self.mess_power = pet_dict[self.kind]["mess_power"]
        self.satiety = 50


class Human:
    def __init__(self, name="Human", car=None, home=None, job=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 100
        self.job = job
        self.home = home
        self.car = car
        self.pet = pet

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_pet(self):
        self.pet = Pet(pet_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 10
            self.home.food -= 5

    def feed_pet(self):
        if self.home.pet_food <= 0:
            self.shopping("pet_food")
        else:
            if self.pet.satiety >= 100:
                print(f"{self.pet.kind} is already full!")
                return
            print(f"Feeding the {self.pet.kind}")
            self.pet.satiety += 20
            self.home.pet_food -= 5
            self.gladness += 5

    def play_with_pet(self):
        print(f"Playing with {self.pet.kind}! So much fun!")
        self.gladness += self.pet.joy
        self.pet.satiety -= 10
        self.home.mess += self.pet.mess_power

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought some fuel!")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("I bought some food for myself")
            self.money -= 50
            self.home.food += 50
        elif manage == "pet_food":
            print(f"I bought food for my {self.pet.kind}")
            self.money -= 30
            self.home.pet_food += 30
        elif manage == "delicacies":
            print("Yay delicacies!")
            self.gladness += 10
            self.satiety += 5
            self.money -= 10

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        print("Cleaning the house...")
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f"Today is the {day} day of {self.name}'s life"
        print(f"{day:^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:-^50}", "\n")
        print(f"Money: {self.money}")
        print(f"Satiety: {self.satiety}")
        print(f"Gladness: {self.gladness}")

        home_indexes = "Home indexes"
        print(f"{home_indexes:-^50}", "\n")
        print(f"Food - {self.home.food}")
        print(f"Pet Food - {self.home.pet_food}")
        print(f"Mess - {self.home.mess}")

        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:-^50}", "\n")
        print(f"Fuel - {self.car.fuel}")
        print(f"Strength - {self.car.strength}")

        if self.pet:
            pet_indexes = f"Pet ({self.pet.kind}) indexes"
            print(f"{pet_indexes:-^50}", "\n")
            print(f"Satiety - {self.pet.satiety}")
        print("=" * 50)

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bankrupt")
            return False
        return True

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I get a job {self.job.job} with salary {self.job.salary}")
        if self.pet is None:
            self.get_pet()
            print(f"I adopted a {self.pet.kind}!")

        self.days_indexes(day)

        self.pet.satiety -= 10
        self.home.mess += 2

        dice = random.randint(1, 6)

        if self.satiety < 20:
            print("I'll go eat")
            self.eat()
        elif self.pet.satiety < 20:
            print("My pet is hungry!")
            self.feed_pet()
        elif self.gladness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                print("Let's play with pet to feel better!")
                self.play_with_pet()
        elif self.money < 0:
            print("Start working")
            self.work()
        elif self.car.strength < 15:
            print("I repair my car")
            self.to_repair()
        elif dice == 1:
            self.chill()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.clean_home()
        elif dice == 4:
            self.shopping(manage="delicacies")
        elif dice == 5:
            self.play_with_pet()
        elif dice == 6:
            self.feed_pet()


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumpition = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel > self.consumpition:
            self.fuel -= self.consumpition
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False


class Home:
    def __init__(self):
        self.mess = 0
        self.food = 0
        self.pet_food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


persona = Human(name="Vasya")
for day in range(1, 15):
    if persona.live(day) == False:
        break
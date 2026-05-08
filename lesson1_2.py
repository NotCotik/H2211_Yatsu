import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 150
        self.alive = True

    def to_study(self):
        print("Time to study!")
        self.progress += 0.12
        self.gladness -= 5

    def to_work(self):
        print("Time to work!")
        self.money += 50
        self.gladness -= 5
        self.progress -= 0.05

    def thoughts_about_faluare(self):
        print("I'm misirable...")
        self.progress -= 0.30
        self.gladness -= 10

    def to_sleep(self):
        print("Good Night")
        self.progress += 0.12
        self.gladness += 3

    def to_chill(self):
        print("Chill time!")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 5

    def is_alive(self):
        if self.progress <= -0.5:
            print("Cast out.....")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression....")
            self.alive = False
        elif self.progress >= 5:
            print("Passed externally...")
            self.alive = False
        elif self.money <= 0:
            print("Broke...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def live(self, day):
        day_str = f"Day {day} of {self.name} life"
        print(f"{day_str:=^50}")

        if self.money < 20:
            self.to_work()
        elif self.progress < 0.1:
            self.to_study()
        else:
            live_cube = random.randint(1, 4)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
            elif live_cube == 4:
                self.thoughts_about_faluare()

        self.end_of_day()
        self.is_alive()


personage = Student(name="Vasya")

for day in range(365):
    if personage.alive == False:
        break
    personage.live(day)
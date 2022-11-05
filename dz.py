import random

class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto()
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
           if self.satiety >= 100:
               self.satiety = 100
            return
                self.satiety += 5
            self.home.food -= 5



    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                self.money -= 5
                return
            self.money += self.job.salary
            self.gladness -= self.job.gladnesss_less
            self.satiety -= 4
    def shopping(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
            if manage == 'fuel':
                print('i bought fuel')
                self.money -= 50
                self.car.fuel += 50
            elif manage == 'food':
                print('bought food')
                self.money -= 25
                self.home.food += 25
            elif manage == 'delicates':
                print('you happy!')
                self.gladness += 10
                self.satiety += 2
                self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strenght += 100
        self.money -= 50
    def days_indexes(self, day):
        day = f'"Today  the {day} of {self.name}'s live"
        print(f'{day:=^50}', '/n')
        humans_indexes = self.name + "'s indexes"
        print(f'{humans_indexes:^50}', '/n')
        print(f'Money = {self.money}')
        print(f'Satiety = {self.satiety}')
        print(f'Gladness = {self.gladness}')
        home_indexes = 'Home indexes'
        print(f'{home_indexes:^50}, '/n')
        print(f'Food = {self.home.food}')
        print(f'Mess = {self.home.mess}')
        car_indexes = f"{self.car.brand} car indexes"
        print(f'{car_indexes:^50}, '/n' )
        print(f'Fuel = {self.car.fuel}')
        print(f'Strenght = {self.car.strenght}')


    def is_alive(self):
        if self.gladness < 0:
            print('Depression')
            return
        if self.satiety < 0:
            print('Dead.....')
        if self.money < -200:
            print('Bankrupt')
            return False
    def live(self):
        if self.is_alive() == False:
            return
        if self.home == None:
            print('Settled in the home ')
            self.get_home()
        if self.car == None:
            self.get_car()
            print(f'I want {self.car.brand}')
        if self.job == None:
            self.get_job()
            print(f'I do not have a job, Im go to get a job {self.job.job}'salary {self.job.salary})
            self.days_indexes(day)


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strenght = brand_list[self.brand]['strenght']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strenght -= 1


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladnesss_less = job_list[self.job]['gladness_less']

brand_of_car = {'BMW':{'fuel': 100, 'strenght': 100, 'consumption': 6},
                'Lada':{'fuel': 50, 'strenght': 40, 'consumption': 10},
                'Volvo':{'fuel': 70, 'strenght': 150, 'consumption': 8},
                'Ferrari':{'fuel': 80, 'strenght': 120, 'consumption': 14}}

job_list = {'Java developer': {'salary': 50, 'gladness_less': 10},
            'Python developer': {'salary': 40, 'gladness_less': 15},
            'C++ developer': {'salary': 55, 'gladness_less': 25},
            'Rust developer': {'salary': 70, 'gladness_less': 1}}
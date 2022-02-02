from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self):
        super().__init__()
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def createCar(self):
        if randint(1, 6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-250, 250))
            self.all_car.append(new_car)

    def moveCar(self):
        for car in self.all_car:
            car.backward(self.car_speed)
    

    def leveUp(self):
        self.car_speed += MOVE_INCREMENT


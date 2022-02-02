from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.goUp, "Up")

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    car_manager.createCar()
    car_manager.moveCar()

    for car in car_manager.all_car:
        if car.distance(player) <20:
            game_is_on = False
            score_board.gameOver()

    if player.isAtFinishLine():
        player.goToStart()
        car_manager.leveUp() 
        score_board.increaseLeve()


screen.exitonclick()

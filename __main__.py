import os
import random

from game.casting.actor import Actor
from game.casting.rock import Rock
from game.casting.gem import Gem
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_services import KeyboardService
from game.services.video_services import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
# Size of window in pixels
MAX_X = 900
MAX_Y = 600
# Setting a grid for size of cells
CELL_SIZE = 15
FONT_SIZE = 15
# How many columns and rows based on cell size - ( MAX_X / CELL_SIZE = COLS )
COLS = 60
ROWS = 40
# What shows up at top of window
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
# Set how many gems and rocks will be created
DEFAULT_GEMS = 15
DEFAULT_ROCKS = 35
STARTING_GAME_SCORE = 0


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner - should be placed in own class
    # This is redunant since we already set these in Actor's __init__
    banner = Actor()
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    # add banner to cast dictionary under key "banners"
    cast.add_actor("banners", banner)
    
    # create the robot - should be placed in own class
    # places robot in center of x, and bottom of y
    x = int(MAX_X / 2)
    y = int(MAX_Y - 15)
    position = Point(x, y)

    # This is redundant since we already set these in the Actor's __init__
    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    # add robot to cast dictionary under key "robots"
    cast.add_actor("robots", robot)

    # create the gems
    # for each gem is range set above:
    for n in range(DEFAULT_GEMS):
        # set image symbol
        text = "*"

        # create random position, created in CELL_SIZE grid (increments of 15)
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        # scales grid back to pixel size
        position = position.scale(CELL_SIZE)

        # setting random red, green, and blue coloring
        """Can be changed to a set color"""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # set everything up and add to cast dictionary in "gems" key
        gem = Gem()
        gem.set_text(text)
        gem.set_font_size(FONT_SIZE)
        # set random color 
        gem.set_color(color)
        # set random position
        gem.set_position(position)
        # grab value
        gem.set_value(1)
        # set velocity - adding value to y so it moves down the screen
        gem.set_velocity(Point(0, 15))
        cast.add_actor("gems", gem)
        
    for n in range(DEFAULT_ROCKS):
        text = "@"

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        rock = Rock()
        rock.set_text(text)
        rock.set_font_size(FONT_SIZE)
        rock.set_color(color)
        rock.set_position(position)
        rock.set_value(1)
        rock.set_velocity(Point(0,5))
        cast.add_actor("rocks", rock)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()
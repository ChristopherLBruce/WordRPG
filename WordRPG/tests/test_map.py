import os
from time import sleep

from WordRPG.gui.screen import Screen
from WordRPG.map import Game_Map
from WordRPG.engine.common import Point



if __name__ == '__main__':
    """ create a 'Game_Map' object using the given image filename and then print
    it to the terminal """
    test_world = Game_Map('test_island2')

    """ prints map as raw tile symbols """
    Screen.setup_terminal(title='MAP TEST', size=test_world.size)
    print(test_world)
    sleep(2)

    # -------------------------------------------------------------------------
    # Draws map using .show()
    # -------------------------------------------------------------------------
    """ Raw alphanumeric characters """
    Screen.setup_terminal(title='MAP TEST', size=test_world.size)
    test_world.show(symbol=False, color=False)
    sleep(2)

    """ ASCII symbols, no color """
    Screen.setup_terminal(title='MAP TEST', size=test_world.size)
    test_world.show(symbol=True, color=False)
    sleep(2)

    """ ASCII symbols, full color """
    Screen.setup_terminal(title='MAP TEST', size=test_world.size)
    test_world.show(symbol=True, color=True)
    sleep(2)

    ## -------------------------------------------------------------------------
    ## Draws map 'frame' using .show()
    ## -------------------------------------------------------------------------
    """ Raw alphanumeric characters """
    size = (40, 20)
    offset = (15, 15)
    test_world.set_map_frame(size)
    Screen.setup_terminal(title='MAP FRAME TEST', size=size)
    test_world.show(frame=True, symbol=True, color=True)
    sleep(2)


    ## -------------------------------------------------------------------------
    ## Scrolling map teests
    ## -------------------------------------------------------------------------
    """ test scrolling map frame """
    size = (40, 20)
    test_world.set_map_frame(size)
    Screen.setup_terminal(title='MAP FRAME TEST', size=size)
    
    vec = (1, 0)
    for _ in range(0, 80):
        test_world.move_frame(vec)
        test_world.show(frame=True, symbol=False, color=False)
        sleep(1.0 / 30)

    """ test scrolling map frame """
    size = (40, 20)
    test_world.set_map_frame(size)
    Screen.setup_terminal(title='MAP FRAME TEST', size=size)
    
    vec = (1, 0)
    for _ in range(0, 80):
        test_world.move_frame(vec)
        test_world.show(frame=True, symbol=True, color=True)
        sleep(1.0 / 30)


    """adding while True loop so terminal stays open until manually closed"""
    while True:
        pass
'''
Hannah Soria
CS151 Visual Media, Fall 2021
Project 4: Zelle Scene and Futurism
'''
import graphics as g
import compound_shapes1 as cs
import time

def main(x,y,scale):
    '''This function calls the shapes created in comoundshapes.py as lists and draws
    them at given x and y coordinates to scale and then animiates them in a while loop.'''
    win=g.GraphWin("scene", 600,600)
    '''This is the window for the scene'''
    win.setBackground("light blue")
    '''This sets the background color'''
    groundList = cs.ground_init(100,100,1)
    for shapes in groundList:
        shapes.draw(win)
    buildingList = cs.building_init(100,300,5)
    for shapes in buildingList:
        shapes.draw(win)
    buildingList = cs.building_init(20,400,3)
    for shapes in buildingList:
        shapes.draw(win)
    buildingList = cs.building_init(500,500,1)
    for shapes in buildingList:
        shapes.draw(win)
    buildingList = cs.building_init(200,250,1)
    for shapes in buildingList:
        shapes.draw(win)
    motorcycleList = cs.motorcycle_init(100,540,1)
    for shapes in motorcycleList:
        shapes.draw(win)
    motorcycleList = cs.motorcycle_init(400,530,2)
    for shapes in motorcycleList:
        shapes.draw(win)
    motorcycleList = cs.motorcycle_init(200,395,.5)
    for shapes in motorcycleList:
        shapes.draw(win)
    motorcycleList = cs.motorcycle_init(400,285,1.5)
    for shapes in motorcycleList:
        shapes.draw(win)
    spaceShipList = cs.spaceShip_init(100,100,1)
    for shapes in spaceShipList:
        shapes.draw(win)
    spaceShipList = cs.spaceShip_init(300,150,2)
    for shapes in spaceShipList:
        shapes.draw(win)
    spaceShipList = cs.spaceShip_init(500,50,.5)
    for shapes in spaceShipList:
        shapes.draw(win)
    alienList = cs.alien_init(290,335,.5)
    for shapes in alienList:
        shapes.draw(win)
    alienList = cs.alien_init(550,190,.8)
    for shapes in alienList:
        shapes.draw(win)
    alienList = cs.alien_init(200,550,.3)
    for shapes in alienList:
        shapes.draw(win)
    alienList = cs.alien_init(250,550,.3)
    for shapes in alienList:
        shapes.draw(win)
    alienList = cs.alien_init(300,550,.3)
    for shapes in alienList:
        shapes.draw(win)
    gunList = cs.gun_init(470,210,.5)
    for shapes in gunList:
        shapes.draw(win)        
    gunList = cs.gun_init(235,327,.5)
    for shapes in gunList:
        shapes.draw(win)
    gunList = cs.gun_init(160,540,.5)
    for shapes in gunList:
        shapes.draw(win)
    catList1 = cs.cat_init(400,220,1.2)
    fishList1 = cs.fish_init(430,160,.7)
    fishList2 = cs.fish_init(205,295,.5)
    fishList3 = cs.fish_init(130,530,.3)
    i = 0
    while True:
        time.sleep(.05)
        cs.cat_animate1(catList1, i, win, 0)
        win.update()
        i = i + 1
        cs.fish_animate(fishList1, i, win, 70)
        i = i + 1
        win.update()
        cs.cat_animate2(catList1, i, win, 120)
        i = i + 1
        win.update()
        cs.cat_animate3(catList1, i, win, 190)
        cs.fish_animate(fishList2, i, win, 210)
        cs.cat_animate4(catList1, i, win, 250)
        cs.cat_animate5(catList1, i, win, 370)
        cs.fish_animate(fishList3, i, win, 390)
        win.update()
        if win.checkMouse():
            break
        
if __name__=='__main__':
    main(0,600,1)

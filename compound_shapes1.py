'''
Hannah Soria
CS151 Visual Media, Fall 2021
Project 4: Zelle Scene and Futurism
'''
import graphics as g
import time
import random as r

def motorcycle_init( x, y, scale):
    '''Creates and returns a list of Zelle Graphics objects to make up a motorcycle.
    Minimally it draws two circle for wheels, an oval for the body, and circle for the front dash, 
    and a rectangle for the handlebar.

    Parameters:
    -----------
    x: int. x coordinate for the circle center of the front wheel.
    y: int. y coordinate for the circle center of the front wheel.
    scale: float. Scaled size of the motorcycle.

    Returns:
    -----------
    list with 5 Zelle objects (circles, oval, rectangle) in it.

    Colors:
    -----------
    Draws the shapes in red or black and outlined in black.
    '''
    radius = 10
    c = g.Circle(g.Point(x, y), radius*scale)
    c.setFill("black")
    c.setOutline("black")
    c.setWidth(1)
    c2 = g.Circle(g.Point(x + 3 * radius * scale, y), radius*scale)
    c2.setFill("black")
    c2.setOutline("black")
    c2.setWidth(1)
    o = g.Oval(g.Point(x - 5 * scale, y - 2 * scale), g.Point(x + 35 * scale, y - 20 *scale))
    o.setFill("red")
    o.setOutline("black")
    o.setWidth(1)
    radius2 = 8
    c3 = g.Circle(g.Point(x - .5 * radius * scale, y - 2.2 * radius * scale), radius2*scale)
    c3.setFill("black")
    c3.setOutline("black")
    c3.setWidth(1)
    r = g.Rectangle(g.Point(x - 5 * scale, y - 28 * scale), g.Point(x + 10 * scale, y - 25 * scale))
    r.setFill("grey")
    r.setOutline("black")
    r.setWidth(1)
    motorcycleList=[c,c2,o,c3,r]
    return (motorcycleList)

def motorcycleTest():
    '''Main function that creates the screen, creates the motorcycle, draws it to the screen.'''
    win=g.GraphWin("motorcycle", 600,600)
    motorcycleList = motorcycle_init(100,100,1)
    for shapes in motorcycleList:
        shapes.draw(win)
    motorcycleList = motorcycle_init(200,200,3)
    for shapes in motorcycleList:
        shapes.draw(win)
    motorcycleList = motorcycle_init(400,400,.5)
    for shapes in motorcycleList:
        shapes.draw(win)
    win.getMouse() # pause for click in window
    win.close()

def spaceShip_init( x, y, scale):
    '''Creates and returns a list of Zelle Graphics objects to make up a spaceship.
    Minimally it draws a circle, an oval, and a polygon stacked and overlapping each other.

    Parameters:
    -----------
    x: int. x coordinate for the circle center of the body of the ship.
    y: int. y coordinate for the circle center of the body of the ship.
    scale: float. Scaled size of the shapceship

    Returns:
    -----------
    list with 3 Zelle objects (circle, oval, polygon) in it.

    Colors:
    -----------
    Draws the shapes in dark green, grey, and silver and outlined in black or grey.
    '''
    radius = 20
    c4 = g.Circle(g.Point(x, y), radius*scale)
    c4.setFill("darkgreen")
    c4.setOutline("black")
    c4.setWidth(1)
    o2 = g.Oval(g.Point(x -30 * scale, y - 15 * scale), g.Point(x + 30 * scale, y +5 *scale))
    o2.setFill("grey")
    o2.setOutline("black")
    o2.setWidth(1)
    p = g.Polygon(g.Point(x - 20 * scale, y - 5 * scale), g.Point(x + 20 * scale, y -5 *scale), g.Point(x + 15 * scale, y - 20 * scale), g.Point(x , y - 27 * scale), g.Point(x - 15 * scale, y - 20 * scale), g.Point(x - 20 * scale, y - 5 * scale))
    p.setFill("silver")
    p.setOutline("grey")
    p.setWidth(2)
    spaceShipList = [c4,o2,p]
    return (spaceShipList)

def spaceShipTest():
    '''Main function that creates the screen, creates the spaceship, draws it to the screen.'''
    win=g.GraphWin("spaceShip", 600,600)
    spaceShipList = spaceShip_init(100,100,1)
    for shapes in spaceShipList:
        shapes.draw(win)
    spaceShipList = spaceShip_init(200,200,2)
    for shapes in spaceShipList:
        shapes.draw(win)
    spaceShipList = spaceShip_init(400,400,.5)
    for shapes in spaceShipList:
        shapes.draw(win)
    win.getMouse() # pause for click in window
    win.close()
  
def building_init( x, y, scale):
    '''Creates and returns a list of Zelle Graphics objects to make up a building.
    Minimally it draws a large rectangle then inside this it draws eight smaller rectangle inside of it.

    Parameters:
    -----------
    x: int. x coordinate for the top right corner of the first rectangle.
    y: int. y coordinate for the top right corner of the first rectangle.
    scale: float. Scaled size of the rectangle.

    Returns:
    -----------
    list with 9 Zelle rectangle objects.

    Colors:
    -----------
    Draws the shapes in brown or yellow and outlined in black.
    '''
    r2 = g.Rectangle(g.Point(x , y ), g.Point(x + 90 * scale, y + 50 * scale))
    r2.setFill("brown")
    r2.setOutline("black")
    r2.setWidth(1)
    r3 = g.Rectangle(g.Point(x + 50 * scale, y + 30 * scale), g.Point(x + 60 * scale, y + 40 * scale))
    r3.setFill("yellow")
    r3.setOutline("black")
    r3.setWidth(1)
    r4 = g.Rectangle(g.Point(x + 50 * scale, y + 10 * scale), g.Point(x + 60 * scale, y + 20 * scale))
    r4.setFill("yellow")
    r4.setOutline("black")
    r4.setWidth(1)
    r5 = g.Rectangle(g.Point(x + 30 * scale, y + 30 * scale), g.Point(x + 40 * scale, y + 40 * scale))
    r5.setFill("yellow")
    r5.setOutline("black")
    r5.setWidth(1)
    r6 = g.Rectangle(g.Point(x +30 * scale, y +10 * scale), g.Point(x + 40 * scale, y + 20 * scale))
    r6.setFill("yellow")
    r6.setOutline("black")
    r6.setWidth(1)
    r7 = g.Rectangle(g.Point(x + 10 * scale, y + 30 * scale), g.Point(x + 20 * scale, y + 40 * scale))
    r7.setFill("yellow")
    r7.setOutline("black")
    r7.setWidth(1)
    r8 = g.Rectangle(g.Point(x + 10 * scale, y + 10 * scale), g.Point(x + 20 * scale, y + 20 * scale))
    r8.setFill("yellow")
    r8.setOutline("black")
    r8.setWidth(1)
    r9 = g.Rectangle(g.Point(x + 70 * scale, y + 30 * scale), g.Point(x + 80 * scale, y + 40 * scale))
    r9.setFill("yellow")
    r9.setOutline("black")
    r9.setWidth(1)
    r10 = g.Rectangle(g.Point(x + 70 * scale, y + 10 * scale), g.Point(x + 80 * scale, y + 20 * scale))
    r10.setFill("yellow")
    r10.setOutline("black")
    r10.setWidth(1)
    buildingList = [r2,r3,r4,r5,r6,r7,r8,r9,r10]
    return (buildingList)

def buildingTest():
    '''Main function that creates the screen, creates the building, draws it to the screen.'''
    win=g.GraphWin("building", 600,600)
    buildingList = building_init(100,100,1)
    for shapes in buildingList:
        shapes.draw(win)
    buildingList = building_init(300,200,3)
    for shapes in buildingList:
        shapes.draw(win)
    buildingList = building_init(500,500,.5)
    for shapes in buildingList:
        shapes.draw(win)
    win.getMouse() # pause for click in window
    win.close()

def alien_init( x, y, scale):
    '''Creates and returns a list of Zelle Graphics objects to make up an alien.
    Minimally it draws two ovals for the head and body, four rectangles for arms and legs,
    four circles for hands and feet, then two ovals and a circle for the face.

    Parameters:
    -----------
    x: int. x coordinate for the upper oval point of the head oval.
    y: int. y coordinate for the upper oval point of the head oval.
    scale: float. Scaled size of the alien.

    Returns:
    -----------
    list with 14 Zelle objects (circles, ovals, rectangles) in it.

    Colors:
    -----------
    Draws the shapes in green or black and outlined in black.
    '''
    r11 = g.Rectangle(g.Point(x - 25 * scale , y - 5 * scale), g.Point(x - 15 * scale, y + 30 * scale))
    r11.setFill("purple")
    r11.setOutline("black")
    r11.setWidth(1)
    o3 = g.Oval(g.Point(x , y ), g.Point(x - 40 * scale, y - 50 *scale))
    o3.setFill("purple")
    o3.setOutline("black")
    o3.setWidth(1)
    r12 = g.Rectangle(g.Point(x - 40 * scale, y + 40 *scale), g.Point(x - 70 * scale, y + 45 * scale))
    r12.setFill("purple")
    r12.setOutline("black")
    r12.setWidth(1)    
    r13 = g.Rectangle(g.Point(x + 5 * scale, y + 40 * scale), g.Point(x + 35 * scale, y + 45 * scale))
    r13.setFill("purple")
    r13.setOutline("black")
    r13.setWidth(1)
    r14 = g.Rectangle(g.Point(x - 25 * scale, y + 90 * scale), g.Point(x - 20 * scale, y + 130 * scale))
    r14.setFill("purple")
    r14.setOutline("black")
    r14.setWidth(1)
    r15 = g.Rectangle(g.Point(x - 15 * scale, y + 90 * scale), g.Point(x - 10 * scale, y + 130 * scale))
    r15.setFill("purple")
    r15.setOutline("black")
    r15.setWidth(1)
    o4 = g.Oval(g.Point(x - 45 * scale, y + 10 * scale), g.Point(x + 8 * scale, y + 100 *scale))
    o4.setFill("purple")
    o4.setOutline("black")
    o4.setWidth(1)
    radius3 = 8
    c5 = g.Circle(g.Point(x - 9 * radius3 * scale, y + 5.5 * radius3 * scale), radius3 * scale)
    c5.setFill("purple")
    c5.setOutline("black")
    c5.setWidth(1)
    c6 = g.Circle(g.Point(x + 5 * radius3 * scale, y + 5.5 * radius3 * scale), radius3 * scale)
    c6.setFill("purple")
    c6.setOutline("black")
    c6.setWidth(1)
    c7 = g.Circle(g.Point(x - 3.3 * radius3 * scale, y + 16 * radius3 * scale), radius3 * scale)
    c7.setFill("purple")
    c7.setOutline("black")
    c7.setWidth(1)
    c8 = g.Circle(g.Point(x - 1.1 * radius3 * scale, y + 16 * radius3 * scale), radius3 * scale)
    c8.setFill("purple")
    c8.setOutline("black")
    c8.setWidth(1)
    o5 = g.Oval(g.Point(x - 30 * scale, y - 20 * scale), g.Point(x - 25 * scale, y - 40 *scale))
    o5.setFill("black")
    o5.setOutline("black")
    o5.setWidth(1)
    o6 = g.Oval(g.Point(x - 10 * scale , y - 20 * scale), g.Point(x -15 * scale, y - 40 *scale))
    o6.setFill("black")
    o6.setOutline("black")
    o6.setWidth(1)
    radius4 = 4
    c9 = g.Circle(g.Point(x - 5 * radius4 * scale, y - 2.5 * radius4 * scale), radius4 * scale)
    c9.setFill("black")
    c9.setOutline("black")
    c9.setWidth(1)
    alienList = [r11,o3,r12,r13,r14,r15,o4,c5,c6,c7,c8,o5,o6,c9]
    return (alienList)

def alienTest():
    '''Main function that creates the screen, creates the alien, draws it to the screen.'''
    win=g.GraphWin("alien", 600,600)
    alienList = alien_init(100,100,2)
    for shapes in alienList:
        shapes.draw(win)
    alienList = alien_init(300,200,1)
    for shapes in alienList:
        shapes.draw(win)
    alienList = alien_init(400,400,.5)
    for shapes in alienList:
        shapes.draw(win)
    win.getMouse() # pause for click in window
    win.close()

def ground_init( x, y , scale):
    '''Creates and returns a list of Zelle Graphics objects to make up a street.
    Minimally it draws a large rectangle for the road then six smaller rectangles
    for the striped line.

    Parameters:
    -----------
    x: int. x coordinate for the top right corner of the street rectangle.
    y: int. y coordinate for the top right corner of the street rectangle.
    scale: float. Scaled size of the ground.

    Returns:
    -----------
    list with 7 Zelle rectangle objects in it.

    Colors:
    -----------
    Draws the shapes in grey or yellow and outlined in black.
    '''
    r16 = g.Rectangle(g.Point(x -100 * scale , y + 450 * scale), g.Point(x + 600 * scale, y + 600 * scale))
    r16.setFill("darkgrey")
    r16.setOutline("black")
    r16.setWidth(1)
    r17 = g.Rectangle(g.Point(x + 100 * scale , y + 475 * scale), g.Point(x + 150 * scale, y + 485 * scale))
    r17.setFill("yellow")
    r17.setOutline("black")
    r17.setWidth(1)
    r18 = g.Rectangle(g.Point(x + 200 * scale , y + 475 * scale), g.Point(x + 250 * scale, y + 485 * scale))
    r18.setFill("yellow")
    r18.setOutline("black")
    r18.setWidth(1)
    r19 = g.Rectangle(g.Point(x + 300 * scale , y + 475 * scale), g.Point(x + 350 * scale, y + 485 * scale))
    r19.setFill("yellow")
    r19.setOutline("black")
    r19.setWidth(1)
    r20 = g.Rectangle(g.Point(x + 400 * scale , y + 475 * scale), g.Point(x + 450 * scale, y + 485 * scale))
    r20.setFill("yellow")
    r20.setOutline("black")
    r20.setWidth(1)
    r21 = g.Rectangle(g.Point(x +500 * scale , y + 475 * scale), g.Point(x + 550 * scale, y + 485 * scale))
    r21.setFill("yellow")
    r21.setOutline("black")
    r21.setWidth(1)
    r22 = g.Rectangle(g.Point(x * scale , y + 475 * scale), g.Point(x + 50 * scale, y + 485 * scale))
    r22.setFill("yellow")
    r22.setOutline("black")
    r22.setWidth(1)
    groundList = [r16,r17,r18,r19,r20,r21,r22]
    return (groundList)

def groundTest():
    '''Main function that creates the screen, creates the ground, draws it to the screen.'''
    win=g.GraphWin("ground", 600,600)
    groundList = ground_init(100,100,1)
    for shapes in groundList:
        shapes.draw(win)
    win.getMouse() # pause for click in window
    win.close()

def cat_init(x,y,scale):
    '''Creates and returns a list of Zelle Graphics objects to make up a cat.
    Minimally it draws two circle for feet, an oval for the body, and circle for the head, 
    and two polygons (triangles) for ears.

    Parameters:
    -----------
    x: int. x coordinate for the corner of the right ear.
    y: int. y coordinate for the corner of the right ear.
    scale: float. Scaled size of the cat.

    Returns:
    -----------
    list with 6 Zelle objects (circles, oval, polygons) in it.

    Colors:
    -----------
    Draws the shapes and outlined in orange.
    '''
    radius5 = 10
    p2 = g.Polygon(g.Point(x + 8 * scale, y + 5 * scale), g.Point(x + 1 * scale, y - 5 *scale), g.Point(x + 1 * scale, y + 5 * scale))
    p2.setFill('orange')
    p2.setOutline('orange')
    p2.setWidth(2)
    p3 = g.Polygon(g.Point(x + 10 * scale, y + 5 * scale), g.Point(x + 17 * scale, y - 5 *scale), g.Point(x + 18 * scale, y + 5 * scale))
    p3.setFill('orange')
    p3.setOutline('orange')
    p3.setWidth(2)
    c10 = g.Circle(g.Point(x + 1 * radius5 * scale, y + 1 * radius5 * scale), radius5 * scale)
    c10.setFill('orange')
    c10.setOutline('orange')
    c10.setWidth(1)
    o7 = g.Oval(g.Point(x + .5 * scale , y + 20 * scale), g.Point(x + 20 * scale, y + 60 * scale))
    o7.setFill('orange')
    o7.setOutline('orange')
    o7.setWidth(1)
    radius6 = 7
    c11 = g.Circle(g.Point(x + 0 * radius6 * scale, y + 8 * radius6 * scale), radius6 * scale)
    c11.setFill('orange')
    c11.setOutline('orange')
    c11.setWidth(1)
    c12 = g.Circle(g.Point(x + 2.5 * radius6 * scale, y + 8 * radius6 * scale), radius6 * scale)
    c12.setFill('orange')
    c12.setOutline('orange')
    c12.setWidth(1)

    catList = [p2,p3, c10,o7,c11,c12]
    return catList

def cat_animate1(shapes, frame, screen, start):
    '''Move the cat at the current iteration of the animation (frame).

    Parameters:
    -----------
    shapes: list with the 5 Zelle Circle objects in it that make up the cat
    frame: int. Current iteration of the animation
    screen: GraphWin. Screen/canvas that the cat is on.
        NOTE: The `screen` is not needed for lab.
    '''
    for shape in shapes:
        if frame == start:
            shape.draw(screen)
        elif frame >= start and frame < start + 120:
            if ((frame + 1) % 2 == 1):
                shape.move (-5,2)
            else:
                shape.move (-5,-2) 

def cat_animate2(shapes, frame, screen, start):
    '''Move the cat at the current iteration of the animation (frame).

    Parameters:
    -----------
    shapes: list with the 5 Zelle Circle objects in it that make up the cat
    frame: int. Current iteration of the animation
    screen: GraphWin. Screen/canvas that the cat is on.
        NOTE: The `screen` is not needed for lab.
    '''
    for shape in shapes:
        if frame == start:
            shape.draw(screen)
        elif frame >= start and frame < start + 70:
            if ((frame + 1) % 2 == 1):
                shape.move (1,5)
            else:
                shape.move (-1,5) 

def cat_animate3(shapes, frame, screen, start):
    '''Move the cat at the current iteration of the animation (frame).

    Parameters:
    -----------
    shapes: list with the 5 Zelle Circle objects in it that make up the cat
    frame: int. Current iteration of the animation
    screen: GraphWin. Screen/canvas that the cat is on.
        NOTE: The `screen` is not needed for lab.
    '''
    for shape in shapes:
        if frame == start:
            shape.draw(screen)
        elif frame >= start and frame < start + 60:
            if ((frame + 1) % 2 == 1):
                shape.move (-5,2)
            else:
                shape.move (-5,-2)

def cat_animate4(shapes, frame, screen, start):
    '''Move the cat at the current iteration of the animation (frame).

    Parameters:
    -----------
    shapes: list with the 5 Zelle Circle objects in it that make up the cat
    frame: int. Current iteration of the animation
    screen: GraphWin. Screen/canvas that the cat is on.
        NOTE: The `screen` is not needed for lab.
    '''
    for shape in shapes:
        if frame == start:
            shape.draw(screen)
        elif frame >= start and frame < start + 120:
            if ((frame + 1) % 2 == 1):
                shape.move (1,5)
            else:
                shape.move (-1,5) 

def cat_animate5(shapes, frame, screen, start):
    '''Move the cat at the current iteration of the animation (frame).

    Parameters:
    -----------
    shapes: list with the 5 Zelle Circle objects in it that make up the cat
    frame: int. Current iteration of the animation
    screen: GraphWin. Screen/canvas that the cat is on.
        NOTE: The `screen` is not needed for lab.
    '''
    for shape in shapes:
        if frame == start:
            shape.draw(screen)
        elif frame >= start and frame < start + 100:
            if ((frame + 1) % 2 == 1):
                shape.move (-5,2)
            else:
                shape.move (-5,-2)

def catTest():
    '''Main function that creates the screen, creates the cat, draws it to the screen.'''
    win=g.GraphWin("cat", 600,600)
    catList = cat_init(100,100,1)
    for shapes in catList:
        shapes.draw(win)
    catList = cat_init(200,200,2)
    for shapes in catList:
        shapes.draw(win)
    catList = cat_init(300,300,.5)
    for shapes in catList:
        shapes.draw(win)
    for i in range(1000):
        time.sleep(.2)
        for shapes in catList:
            cat_animate1(catList, i, win)
            win.update()
        if win.checkMouse():
            break
    win.getMouse()  
    win.close()

def gun_init(x,y,scale):
    '''Creates and returns a list of Zelle Graphics objects to make up a gun.
    Minimally it draws two rectangles to make up the gun.

    Parameters:
    -----------
    x: int. x coordinate for the upper left of the body of the gun.
    y: int. y coordinate for the cupper left of the body of the gun.
    scale: float. Scaled size of the gun.

    Returns:
    -----------
    list with 2 Zelle objects (rectangles) in it.

    Colors:
    -----------
    Draws the shapes in grey and outlined in black.
    '''
    r23 = g.Rectangle(g.Point(x + 5 * scale , y + 10 * scale), g.Point(x + 40 * scale, y + 30 * scale))
    r23.setFill("silver")
    r23.setOutline("black")
    r23.setWidth(1)
    r24 = g.Rectangle(g.Point(x + 40 * scale , y + 30 * scale), g.Point(x + 30 * scale, y + 50 * scale))
    r24.setFill("silver")
    r24.setOutline("black")
    r24.setWidth(1)
    gunList = [r23,r24]
    return gunList

def gunTest():
    '''Main function that creates the screen, creates the gun, draws it to the screen.'''
    win=g.GraphWin("gun", 600,600)
    gunList = gun_init(100,100,1)
    for shapes in gunList:
        shapes.draw(win)
    gunList = gun_init(200,200,.5)
    for shapes in gunList:
        shapes.draw(win)
    gunList = gun_init(300,300,2)
    for shapes in gunList:
        shapes.draw(win)
    win.getMouse()
    win.close()

def fish_init(x,y,scale):
    '''Creates and returns a list of Zelle Graphics objects to make up a fish.
    Minimally it draws a circle and triangle to make up the fish.

    Parameters:
    -----------
    x: int. x coordinate for the upper left of the tail.
    y: int. y coordinate for the upper left of the tail.
    scale: float. Scaled size of the tail.

    Returns:
    -----------
    list with 2 Zelle objects (circle, triangle) in it.

    Colors:
    -----------
    Draws the shapes in and outlined in black.
    '''
    p4 = g.Polygon(g.Point(x + 45 * scale, y + 70 * scale), g.Point(x + 35 * scale, y + 80 *scale), g.Point(x + 45 * scale, y + 90 * scale))
    p4.setFill("black")
    p4.setOutline("black")
    p4.setWidth(2)
    radius7 = 10
    c13 = g.Circle(g.Point(x + 2.5 * radius7 * scale, y + 8 * radius7 * scale), radius7 * scale)
    c13.setFill("black")
    c13.setOutline("black")
    c13.setWidth(1)
    fishList = [p4,c13]
    return fishList

def fish_animate(shapes, frame, screen, start):
    '''Move the fish at the current iteration of the animation (frame).

    Parameters:
    -----------
    shapes: list with the 5 Zelle Circle objects in it that make up the fish
    frame: int. Current iteration of the animation
    screen: GraphWin. Screen/canvas that the fish is on.
        NOTE: The `screen` is not needed for lab.
    '''

    for shape in shapes:
        if frame == start:
            shape.draw(screen)
        elif frame >start and frame < start + 1000:
            if ((frame + 1) % 2 == 1):
                shape.move (-5,5)
            else:
                shape.move (-5,-5)

def fishTest():
    '''Main function that creates the screen, creates the fish draws it to the screen.'''
    win=g.GraphWin("fish", 600,600)
    fishList = fish_init(100,100,1)
    for shapes in fishList:
        shapes.draw(win)
    fishList = fish_init(200,200,.5)
    for shapes in fishList:
        shapes.draw(win)
    fishList = fish_init(300,300,2)
    for shapes in fishList:
        shapes.draw(win)
    for i in range(1000):
        time.sleep(.5)
        for shapes in fishList:
            fish_animate(fishList, i, win)
            win.update()
        if win.checkMouse():
            break
    win.getMouse() # pause for click in window
    win.close()

if __name__=='__main__':
    motorcycleTest()
    spaceShipTest()
    buildingTest()
    alienTest()
    groundTest()
    gunTest()
    fishTest()
    catTest()

    



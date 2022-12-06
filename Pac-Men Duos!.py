#Gabe King GK, Owen Wilson OW, Teo Stoilevski TS
#import necessary libraries
from random import choice
from turtle import *
from freegames import floor, vector
#take input for gamemode, map and pacman's colour
gamemode=str(input("Enter 1 for co-op or 2 for evil Pacman/versus:"))
choosemap=str(input("Enter map choice (classic, space, bullseye, western):"))
choosecolour=str(input("Enter a colour for Pacman (yellow, blue, orange, purple):"))
paccolour=choosecolour.strip(' ')
#tests for valid colour input
if paccolour != 'yellow' and paccolour != 'blue' and paccolour != 'orange' and paccolour != 'purple':
    print ('Not a valid colour')
#list of colours and their turtle id's
yellow='gold1'
blue='steelblue2'
orange='darkorange2'
purple='purple'
pink='hotpink'
green='seagreen1'
violet='slateblue2'
brown='tomato4'

#case where gamemode is co-op
if gamemode=='1':
    #input for the second pacmans colours
    choosecolour1=str(input("Enter a colour for second Pacman (pink,green,violet,brown):"))
    paccolour1=choosecolour1.strip(' ')
    #tests if colour is valid
    if paccolour1 != 'pink' and paccolour1 != 'green' and paccolour1 != 'violet' and paccolour1 != 'brown':
        print ('Not a valid colour')
    #case where classic map is chosen
    if choosemap=='classic':
        #score
        state = {'score': 0}
        #writer for the path pacman/the ghosts can go on 
        path = Turtle(visible=False)
        #writer for the score
        writer = Turtle(visible=False)
        #arrow key pacmans aim vector
        aim = vector(0, 0)
        #w,a,s,d pacmans aim vector
        aim1= vector(0, 0)
        #spawn location vectors and initial speed vectors for ghosts only
        pacman = vector(-40, -80)
        pacman1 = vector(-40, -80)
        ghost1 = vector(-180, 160), vector(10, 0)
        ghost2 = vector(-180, -160), vector(0, 10)
        ghost3 = vector(100, 160), vector(0, -10)
        ghost4 = vector(100, -160), vector(-10, 0)
        
        #defining the map: 1 is avalid path, 0 is an invalid path
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
    
        #draw square using a path at point (x,y)
        def square(x, y):
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
        #returns the offset of point in tiles
        def offset(point):
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
        #tests if the tile is valid for pacman and ghosts to go on
        def valid(point):
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
        #defines the world, makes a square background and the path writer over the 1s in tiles
        def world():
            bgcolor('midnightblue')
            path.color('black')
            
            for index in range(len(tiles)):
                tile = tiles[index]
    
                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)
    
                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(4, 'salmon')
    
        #moves pacman and all of the ghosts/writers
        def move():
            #writes score
            writer.undo()
            writer.write(state['score'],font =('Courier',20,'bold'))
    
            clear()
            #tests if direction arrow pacman is aimed is valid
            if valid(pacman + aim):
                pacman.move(aim)
    
            index = offset(pacman)
            
            #defines when tiles=1, adds to score and redifines them so the pellet is gone
            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
           
            #moves arrow pacman / defines shape, colour, and size
            up()
            goto(pacman.x + 10, pacman.y + 10)
            dot(25, paccolour)
            
            #tests if direction w,a,s,d pacman is aimed is valid
            if valid(pacman1 + aim1):
                pacman1.move(aim1)
    
            index = offset(pacman1)
    
            #defines when tiles=1, adds to score and redifines them so the pellet is gone
            if tiles[index] == 1: 
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
    
            #moves w,a,s,d pacman / defines shape, colour, and size
            up()
            goto(pacman1.x + 10, pacman1.y + 10)
            dot(25, paccolour1)
            
            #tests if direction ghost is headed is valid
            #if valid the ghost chooses a vector and follows it
            for point, course in ghost1, ghost2, ghost3, ghost4:
                if valid(point + course):
                    point.move(course)
            #if not valid the ghosts will choose from options and begin a new course
                else:
                    options = [
                        vector(10, 0),
                        vector(-10, 0),
                        vector(0, 10),
                        vector(0, -10),
                    ]
                    plan = choice(options)
                    course.x = plan.x
                    course.y = plan.y
            #executes the course and moves ghost/defines size and colour
                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'red')
    
            update()
            #if distance between pacman and ghost gets too small: game ends and prints the following
            for point, course in ghost1, ghost2, ghost3, ghost4:
                if abs(pacman - point) < 20 or abs(pacman1 - point) < 20:
                    print()
                    print ('You Died:(') 
                    points=str(state)
                    print()
                    print ('Your Score:'+points.strip('{\'score\':}'))
                    exit()
            #if all points are collected: prints the following
            if str(state).strip('{\'score\':}')=='160':
                print()
                print('Congratulations! You Won!')
                points=str(state)
                print ('Your Score:'+points.strip('{\'score\':}'))
                exit()
            #pauses then starts and allows movement
            ontimer(move, 100)
    
        #Change arrow pacman aim if valid
        def change(x, y):
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        #Change w,a,s,d pacman aim if valid
        def change1(x1, y1):            
            if valid(pacman1 + vector(x1, y1)):
                aim1.x = x1
                aim1.y = y1
        #Defines position of the map   
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        #Defines the colour and position of score counter
        writer.color('midnightblue')
        writer.goto(160, 160)
        writer.color('salmon')
        writer.write(state['score'])
        #Listens for key clicks and takes as input to move pacman
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        onkey(lambda: change1(5, 0), 'd')
        onkey(lambda: change1(-5, 0), 'a')
        onkey(lambda: change1(0, 5), 'w')
        onkey(lambda: change1(0, -5), 's')
        world()
        move()
        done()
    
    #Case where space map is chosen
    #Same conditions as previous map
    elif choosemap=='space':
        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(0, 0)
        aim1= vector(0, 0)
        pacman = vector(-40, -80)
        pacman1 = vector(-40, -80)
        ghost1 = vector(-180, 160), vector(5, 0)
        ghost2 = vector(-180, -160), vector(0, 5)
        ghost3 = vector(100, 160), vector(0, -5)
        ghost4 = vector(100, -160), vector(-5, 0)
        ghost5 = vector(-80, 80), vector(0,5)
        ghost6 = vector (-20, 80), vector(0,5)
    
        # fmt: off
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        # fmt: on
        
        
        def square(x, y):
            
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
           
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
           
            bgcolor('black')
            path.color('gray50')
    
            for index in range(len(tiles)):
                tile = tiles[index]
    
                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)
    
                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(8, 'purple4')
    
    
        def move():
            
            writer.undo()
            writer.write(state['score'],font =('Courier',20,'bold'))
    
            clear()
    
            if valid(pacman + aim):
                pacman.move(aim)
    
            index = offset(pacman)
    
            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
    
            up()
            goto(pacman.x + 10, pacman.y + 10)
            dot(25, paccolour)
            
            
            if valid(pacman1 + aim1):
                pacman1.move(aim1)
    
            index = offset(pacman1)
    
            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
    
            up()
            goto(pacman1.x + 10, pacman1.y + 10)
            dot(25, paccolour1)
            
            for point, course in ghost1, ghost2, ghost3, ghost4, ghost5, ghost6:
                if valid(point + course):
                    point.move(course)
                else:
                    options = [
                        vector(10, 0),
                        vector(-10, 0),
                        vector(0, 10),
                        vector(0, -10),
                    ]
                    plan = choice(options)
                    course.x = plan.x
                    course.y = plan.y
    
                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'firebrick4')
    
            update()
    
            for point, course in ghost1, ghost2, ghost3, ghost4, ghost5, ghost6:
                if abs(pacman - point) < 20 or abs(pacman1 - point) < 20:
                    print()
                    print ('You Died:(') 
                    points=str(state)
                    print ('Your Score:'+points.strip('{\'score\':}'))
                    exit()
            if str(state).strip('{\'score\':}')=='170':
                print()
                print('Congratulations! You Won!')
                points=str(state)
                print ('Your Score:'+points.strip('{\'score\':}'))
                exit()
    
            ontimer(move, 100)
    
    
        def change(x, y):
            
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            
            if valid(pacman1 + vector(x1, y1)):
                aim1.x = x1
                aim1.y = y1
    
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        writer.color('black')
        writer.goto(160, 160)
        writer.color('white')
        writer.write(state['score'])
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        onkey(lambda: change1(5, 0), 'd')
        onkey(lambda: change1(-5, 0), 'a')
        onkey(lambda: change1(0, 5), 'w')
        onkey(lambda: change1(0, -5), 's')
        world()
        move()
        done()
    
    #Case where bullseye map is chosen
    #Same conditions as previous map
    elif choosemap=='bullseye':
        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(0, 0)
        aim1= vector(0, 0)
        pacman = vector(-40, -80)
        pacman1 = vector(-40, -80)
        ghost1 = vector(-180, 160), vector(5, 0)
        ghost2 = vector(-140, -120), vector(0, 5)
        ghost3 = vector(20, 80), vector(0, -5)
        ghost4 = vector(-20, -20), vector(-5, 0)
        ghost5 = vector(100, -160), vector (-5, 0)

        # fmt: off
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            ]
        # fmt: on
        
        
        def square(x, y):
            
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            
            bgcolor('red4')
            path.color('GhostWhite')
    
            for index in range(len(tiles)):
                tile = tiles[index]
    
                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)
    
                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(4, 'black')
    
    
        def move():
            
            writer.undo()
            writer.write(state['score'],font =('Courier',20,'bold'))
    
            clear()
    
            if valid(pacman + aim):
                pacman.move(aim)
    
            index = offset(pacman)
    
            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
    
            up()
            goto(pacman.x + 10, pacman.y + 10)
            dot(25, paccolour)
            
            
            if valid(pacman1 + aim1):
                pacman1.move(aim1)
    
            index = offset(pacman1)
    
            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
    
            up()
            goto(pacman1.x + 10, pacman1.y + 10)
            dot(25, paccolour1)
            
            for point, course in ghost1, ghost2, ghost3, ghost4, ghost5:
                if valid(point + course):
                    point.move(course)
                else:
                    options = [
                        vector(5, 0),
                        vector(-5, 0),
                        vector(0, 5),
                        vector(0, -5),
                    ]
                    plan = choice(options)
                    course.x = plan.x
                    course.y = plan.y
    
                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'firebrick1')
    
            update()
    
            for point, course in ghost1, ghost2, ghost3, ghost4, ghost5:
                if abs(pacman - point) < 20 or abs(pacman1 - point) < 20:
                    print()
                    print ('You Died:(') 
                    points=str(state)
                    print ('Your Score:'+points.strip('{\'score\':}'))
                    exit()
            if str(state).strip('{\'score\':}')=='159':
                print()
                print('Congratulations! You Won!')
                points=str(state)
                print ('Your Score:'+points.strip('{\'score\':}'))
                exit()
    
            ontimer(move, 100)
    
    
        def change(x, y):
            
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            
            if valid(pacman1 + vector(x1, y1)):
                aim1.x = x1
                aim1.y = y1
    
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        writer.color('red4')
        writer.goto(160, 160)
        writer.color('GhostWhite')
        writer.write(state['score'])
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        onkey(lambda: change1(5, 0), 'd')
        onkey(lambda: change1(-5, 0), 'a')
        onkey(lambda: change1(0, 5), 'w')
        onkey(lambda: change1(0, -5), 's')
        world()
        move()
        done()
    
    #Case where western map is chosen
    #Same conditions as previous map    
    elif choosemap=='western':
        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(0, 0)
        aim1= vector(0, 0)
        pacman = vector(-20, -80)
        pacman1 = vector(-20, -80)
        ghost1 = vector(-180, 140), vector(10, 0)
        ghost2 = vector(-180, -140), vector(0, 10)
        ghost3 = vector(100, 160), vector(0, -10)
        ghost4 = vector(100, -140), vector(-10, 0)
    
        # fmt: off
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        # fmt: on
        
        
        def square(x, y):
            
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            
            bgcolor('sienna4')
            path.color('tan2')
    
            for index in range(len(tiles)):
                tile = tiles[index]
    
                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)
    
                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(6, 'DarkGreen')
    
    
        def move():
            
            writer.undo()
            writer.write(state['score'],font =('Courier',20,'bold'))
    
            clear()
    
            if valid(pacman + aim):
                pacman.move(aim)
    
            index = offset(pacman)
    
            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
    
            up()
            goto(pacman.x + 10, pacman.y + 10)
            dot(25, paccolour)
            
            
            if valid(pacman1 + aim1):
                pacman1.move(aim1)
    
            index = offset(pacman1)
    
            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
    
            up()
            goto(pacman1.x + 10, pacman1.y + 10)
            dot(25, paccolour1)
            
            for point, course in ghost1, ghost2, ghost3, ghost4:
                if valid(point + course):
                    point.move(course)
                else:
                    options = [
                        vector(10, 0),
                        vector(-10, 0),
                        vector(0, 10),
                        vector(0, -10),
                    ]
                    plan = choice(options)
                    course.x = plan.x
                    course.y = plan.y
    
                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'indianred4')
    
            update()
    
            for point, course in ghost1, ghost2, ghost3, ghost4:
                if abs(pacman - point) < 20 or abs(pacman1 - point) < 20:
                    print()
                    print ('You Died:(') 
                    points=str(state)
                    print ('Your Score:'+points.strip('{\'score\':}'))
                    exit()
            if str(state).strip('{\'score\':}')=='170':
                print()
                print('Congratulations! You Won!')
                points=str(state)
                print ('Your Score:'+points.strip('{\'score\':}'))
                exit()
    
            ontimer(move, 100)
    
    
        def change(x, y):
            
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            
            if valid(pacman1 + vector(x1, y1)):
                aim1.x = x1
                aim1.y = y1
    
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        writer.color('sienna4')
        writer.goto(160, 160)
        writer.color('black')
        writer.write(state['score'])
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        onkey(lambda: change1(5, 0), 'd')
        onkey(lambda: change1(-5, 0), 'a')
        onkey(lambda: change1(0, 5), 'w')
        onkey(lambda: change1(0, -5), 's')
        world()
        move()
        done()
    
    #If invalid map is input, prints following statement  
    else:
        print('Not valid map')

#Case where gamemode 2 is chosen
#Same conditions as previous gamemode
elif gamemode=='2':
    if choosemap=='classic':
        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(0, 0)
        aim1= vector(0, 0)
        pacman = vector(-40, -80)
        pacman1 = vector(100, -160)
        ghost1 = vector(-180, 160), vector(5, 0)
        ghost2 = vector(-180, -160), vector(0, 5)
        ghost3 = vector(100, 160), vector(0, -5)
    
        # fmt: off
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        # fmt: on
    
    
        def square(x, y):
           
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            
            bgcolor('midnightblue')
            path.color('black')
    
            for index in range(len(tiles)):
                tile = tiles[index]
    
                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)
    
                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(4, 'salmon')
    
    
        def move():
          
            writer.undo()
            writer.write(state['score'],font =('Courier',20,'bold'))
    
            clear()
    
            if valid(pacman + aim):
                pacman.move(aim)
    
            index = offset(pacman)
    
            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
    
            up()
            goto(pacman.x + 10, pacman.y + 10)
            dot(25, paccolour)
            
            
            if valid(pacman1 + aim1):
                pacman1.move(aim1)
    
            up()
            goto(pacman1.x + 10, pacman1.y + 10)
            dot(25, 'orangered4')
            
            for point, course in ghost1, ghost2, ghost3:
                if valid(point + course):
                    point.move(course)
                else:
                    options = [
                        vector(5, 0),
                        vector(-5, 0),
                        vector(0, 5),
                        vector(0, -5),
                    ]
                    plan = choice(options)
                    course.x = plan.x
                    course.y = plan.y
    
                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'red')
    
            update()
    
            for point, course in ghost1, ghost2, ghost3:
                if abs(pacman - point) < 20:
                    print()
                    print ('Evil Pac-man Wins') 
                    points=str(state)
                    print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                    exit()
            if abs(pacman-pacman1) <20:
                print()
                print ('Evil Pac-man Wins') 
                points=str(state)
                print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                exit()
            if str(state).strip('{\'score\':}')=='160':
                print()
                print ('Good Pac-man Wins') 
                points=str(state)
                print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                exit()
    
            ontimer(move, 100)
    
    
        def change(x, y):
            
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            
            if valid(pacman1 + vector(x1, y1)):
                aim1.x = x1
                aim1.y = y1
    
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        writer.color('midnightblue')
        writer.goto(160, 160)
        writer.color('salmon')
        writer.write(state['score'])
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        onkey(lambda: change1(5, 0), 'd')
        onkey(lambda: change1(-5, 0), 'a')
        onkey(lambda: change1(0, 5), 'w')
        onkey(lambda: change1(0, -5), 's')
        world()
        move()
        done()
    
    elif choosemap=='space':
        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(0, 0)
        aim1= vector(0, 0)
        pacman = vector(-40, -80)
        pacman1 = vector(-20, 80)
        ghost1 = vector(-180, 160), vector(5, 0)
        ghost2 = vector(-180, -160), vector(0, 5)
        ghost3 = vector(100, 160), vector(0, -5)
        ghost4 = vector(100, -160), vector(-5, 0)
        ghost5 = vector(-80, 80), vector(0,5)
    
        # fmt: off
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        # fmt: on
    
    
        def square(x, y):
            
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
           
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            
            bgcolor('black')
            path.color('gray50')
    
            for index in range(len(tiles)):
                tile = tiles[index]
    
                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)
    
                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(8, 'purple4')
    
    
        def move():
           
            writer.undo()
            writer.write(state['score'],font =('Courier',20,'bold'))
    
            clear()
    
            if valid(pacman + aim):
                pacman.move(aim)
    
            index = offset(pacman)
    
            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
    
            up()
            goto(pacman.x + 10, pacman.y + 10)
            dot(25, paccolour)
            
            
            if valid(pacman1 + aim1):
                pacman1.move(aim1)
    
            up()
            goto(pacman1.x + 10, pacman1.y + 10)
            dot(25, 'DarkRed')
            
            for point, course in ghost1, ghost2, ghost3, ghost4, ghost5:
                if valid(point + course):
                    point.move(course)
                else:
                    options = [
                        vector(5, 0),
                        vector(-5, 0),
                        vector(0, 5),
                        vector(0, -5),
                    ]
                    plan = choice(options)
                    course.x = plan.x
                    course.y = plan.y
    
                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'firebrick4')
    
            update()
    
            for point, course in ghost1, ghost2, ghost3, ghost4, ghost5:
                if abs(pacman - point) < 20:
                    print()
                    print ('Evil Pac-man Wins') 
                    points=str(state)
                    print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                    exit()
            if abs(pacman-pacman1) <20:
                print()
                print ('Evil Pac-man Wins') 
                points=str(state)
                print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                exit()
            if str(state).strip('{\'score\':}')=='170':
                print()
                print ('Good Pac-man Wins') 
                points=str(state)
                print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                exit()
    
            ontimer(move, 100)
    
    
        def change(x, y):
            
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            
            if valid(pacman1 + vector(x1, y1)):
                aim1.x = x1
                aim1.y = y1
    
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        writer.color('black')
        writer.goto(160, 160)
        writer.color('white')
        writer.write(state['score'])
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        onkey(lambda: change1(5, 0), 'd')
        onkey(lambda: change1(-5, 0), 'a')
        onkey(lambda: change1(0, 5), 'w')
        onkey(lambda: change1(0, -5), 's')
        world()
        move()
        done()
    
    elif choosemap=='bullseye':
        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(0, 0)
        aim1= vector(0, 0)
        pacman = vector(-40, -80)
        pacman1 = vector(-180, 160)
        ghost2 = vector(-140, -120), vector(0, 5)
        ghost3 = vector(20, 80), vector(0, -5)
        ghost1 = vector(-20, -20), vector(-5, 0)

        # fmt: off
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            ]
        # fmt: on
        def square(x, y):
            
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            
            bgcolor('red4')
            path.color('GhostWhite')
    
            for index in range(len(tiles)):
                tile = tiles[index]
    
                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)
    
                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(4, 'black')
    
    
        def move():
            
            writer.undo()
            writer.write(state['score'],font =('Courier',20,'bold'))
    
            clear()
    
            if valid(pacman + aim):
                pacman.move(aim)
    
            index = offset(pacman)
    
            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
    
            up()
            goto(pacman.x + 10, pacman.y + 10)
            dot(25, paccolour)
            
            
            if valid(pacman1 + aim1):
                pacman1.move(aim1)
    
            up()
            goto(pacman1.x + 10, pacman1.y + 10)
            dot(25, 'orangered4')
            
            for point, course in ghost1, ghost2, ghost3:
                if valid(point + course):
                    point.move(course)
                else:
                    options = [
                        vector(5, 0),
                        vector(-5, 0),
                        vector(0, 5),
                        vector(0, -5),
                    ]
                    plan = choice(options)
                    course.x = plan.x
                    course.y = plan.y
    
                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'firebrick1')
    
            update()
    
            for point, course in ghost1, ghost2, ghost3:
                if abs(pacman - point) < 20:
                    print()
                    print ('Evil Pac-man Wins') 
                    points=str(state)
                    print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                    exit()
            if abs(pacman-pacman1) <20:
                print()
                print ('Evil Pac-man Wins') 
                points=str(state)
                print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                exit()
            if str(state).strip('{\'score\':}')=='159':
                print()
                print ('Good Pac-man Wins') 
                points=str(state)
                print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                exit()
    
            ontimer(move, 100)
    
    
        def change(x, y):
            
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            
            if valid(pacman1 + vector(x1, y1)):
                aim1.x = x1
                aim1.y = y1
    
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        writer.color('red4')
        writer.goto(160, 160)
        writer.color('GhostWhite')
        writer.write(state['score'])
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        onkey(lambda: change1(5, 0), 'd')
        onkey(lambda: change1(-5, 0), 'a')
        onkey(lambda: change1(0, 5), 'w')
        onkey(lambda: change1(0, -5), 's')
        world()
        move()
        done()
        
    elif choosemap=='western':
        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(0, 0)
        aim1= vector(0, 0)
        pacman = vector(-40, -80)
        pacman1 = vector(100, -160)
        ghost1 = vector(-180, 160), vector(5, 0)
        ghost2 = vector(-180, -160), vector(0, 5)
        ghost3 = vector(100, 160), vector(0, -5)
    
        # fmt: off
        tiles = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
            0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0,
            0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
            0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ]
        # fmt: on
    
    
        def square(x, y):
            
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
           
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
           
            bgcolor('sienna4')
            path.color('tan2')
    
            for index in range(len(tiles)):
                tile = tiles[index]
    
                if tile > 0:
                    x = (index % 20) * 20 - 200
                    y = 180 - (index // 20) * 20
                    square(x, y)
    
                    if tile == 1:
                        path.up()
                        path.goto(x + 10, y + 10)
                        path.dot(6, 'DarkGreen')
    
    
        def move():
            
            writer.undo()
            writer.write(state['score'],font =('Courier',20,'bold'))
    
            clear()
    
            if valid(pacman + aim):
                pacman.move(aim)
    
            index = offset(pacman)
    
            if tiles[index] == 1:
                tiles[index] = 2
                state['score'] += 1
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
    
            up()
            goto(pacman.x + 10, pacman.y + 10)
            dot(25, paccolour)
            
            
            if valid(pacman1 + aim1):
                pacman1.move(aim1)
    
            up()
            goto(pacman1.x + 10, pacman1.y + 10)
            dot(25, 'brown')
            
            for point, course in ghost1, ghost2, ghost3:
                if valid(point + course):
                    point.move(course)
                else:
                    options = [
                        vector(5, 0),
                        vector(-5, 0),
                        vector(0, 5),
                        vector(0, -5),
                    ]
                    plan = choice(options)
                    course.x = plan.x
                    course.y = plan.y
    
                up()
                goto(point.x + 10, point.y + 10)
                dot(20, 'indianred4')
    
            update()
    
            for point, course in ghost1, ghost2, ghost3:
                if abs(pacman - point) < 20:
                    print()
                    print ('Evil Pac-man Wins') 
                    points=str(state)
                    print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                    exit()
            if abs(pacman-pacman1) <20:
                print()
                print ('Evil Pac-man Wins') 
                points=str(state)
                print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                exit()
            if str(state).strip('{\'score\':}')=='160':
                print()
                print ('Good Pac-man Wins') 
                points=str(state)
                print ('Good Pac-Man\'s Score:'+points.strip('{\'score\':}'))
                exit()
    
            ontimer(move, 100)
    
    
        def change(x, y):
            
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            
            if valid(pacman1 + vector(x1, y1)):
                aim1.x = x1
                aim1.y = y1
    
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        writer.color('sienna4')
        writer.goto(160, 160)
        writer.color('black')
        writer.write(state['score'])
        listen()
        onkey(lambda: change(5, 0), 'Right')
        onkey(lambda: change(-5, 0), 'Left')
        onkey(lambda: change(0, 5), 'Up')
        onkey(lambda: change(0, -5), 'Down')
        onkey(lambda: change1(5, 0), 'd')
        onkey(lambda: change1(-5, 0), 'a')
        onkey(lambda: change1(0, 5), 'w')
        onkey(lambda: change1(0, -5), 's')
        world()
        move()
        done()
        
    else:
        print('Not valid map')

#If invalid gamemode is input, prints following string
else:
    print('Not valid input for gamemode')

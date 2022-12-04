from random import choice
from turtle import *
from freegames import floor, vector
gamemode=str(input("Enter 1 for co-op or 2 for evil Pacman/versus:"))
choosemap=str(input("Enter map choice (classic, space, bullseye, western):"))
choosecolour=str(input("Enter a colour for Pacman (yellow, blue, orange, purple):"))
paccolour=choosecolour.strip(' ')
if paccolour != 'yellow' and paccolour != 'blue' and paccolour != 'orange' and paccolour != 'purple':
    print ('Not a valid colour')
yellow='gold1'
blue='steelblue2'
orange='darkorange2'
purple='purple'
pink='hotpink'
green='seagreen1'
violet='slateblue2'
brown='tomato4'

if gamemode=='1':
    choosecolour1=str(input("Enter a colour for second Pacman (pink,green,violet,brown):"))
    paccolour1=choosecolour1.strip(' ')
    if paccolour1 != 'pink' and paccolour1 != 'green' and paccolour1 != 'violet' and paccolour1 != 'brown':
        print ('Not a valid colour')
    if choosemap=='classic':
        state = {'score': 0}
        path = Turtle(visible=False)
        writer = Turtle(visible=False)
        aim = vector(0, 0)
        aim1= vector(0, 0)
        pacman = vector(-40, -80)
        pacman1 = vector(-40, -80)
        ghost1 = vector(-180, 160), vector(10, 0)
        ghost2 = vector(-180, -160), vector(0, 10)
        ghost3 = vector(100, 160), vector(0, -10)
        ghost4 = vector(100, -160), vector(-10, 0)
    
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
            """Draw square using path at (x, y)."""
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            """Return offset of point in tiles."""
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            """Return True if point is valid in tiles."""
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            """Draw world using path."""
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
            """Move pacmasn and all ghosts."""
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
                dot(20, 'red')
    
            update()
    
            for point, course in ghost1, ghost2, ghost3, ghost4:
                if abs(pacman - point) < 20 or abs(pacman1 - point) < 20:
                    print()
                    print ('You Died:(') 
                    points=str(state)
                    print()
                    print ('Your Score:'+points.strip('{\'score\':}'))
                    exit()
            if str(state).strip('{\'score\':}')=='160':
                print()
                print('Congratulations! You Won!')
                points=str(state)
                print ('Your Score:'+points.strip('{\'score\':}'))
                exit()
    
            ontimer(move, 100)
    
    
        def change(x, y):
            """Change pacman aim if valid."""
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            """Change pacman aim if valid."""
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
            """Draw square using path at (x, y)."""
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            """Return offset of point in tiles."""
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            """Return True if point is valid in tiles."""
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            """Draw world using path."""
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
            """Move pacmasn and all ghosts."""
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
            """Change pacman aim if valid."""
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            """Change pacman aim if valid."""
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
            """Draw square using path at (x, y)."""
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            """Return offset of point in tiles."""
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            """Return True if point is valid in tiles."""
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            """Draw world using path."""
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
            """Move pacmasn and all ghosts."""
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
            """Change pacman aim if valid."""
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            """Change pacman aim if valid."""
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
            """Draw square using path at (x, y)."""
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            """Return offset of point in tiles."""
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            """Return True if point is valid in tiles."""
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            """Draw world using path."""
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
            """Move pacmasn and all ghosts."""
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
            """Change pacman aim if valid."""
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            """Change pacman aim if valid."""
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
            """Draw square using path at (x, y)."""
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            """Return offset of point in tiles."""
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            """Return True if point is valid in tiles."""
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            """Draw world using path."""
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
            """Move pacmasn and all ghosts."""
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
            """Change pacman aim if valid."""
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            """Change pacman aim if valid."""
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
            """Draw square using path at (x, y)."""
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            """Return offset of point in tiles."""
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            """Return True if point is valid in tiles."""
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            """Draw world using path."""
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
            """Move pacmasn and all ghosts."""
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
            """Change pacman aim if valid."""
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            """Change pacman aim if valid."""
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
            """Draw square using path at (x, y)."""
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            """Return offset of point in tiles."""
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            """Return True if point is valid in tiles."""
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            """Draw world using path."""
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
            """Move pacmasn and all ghosts."""
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
            """Change pacman aim if valid."""
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            """Change pacman aim if valid."""
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
            """Draw square using path at (x, y)."""
            path.up()
            path.goto(x, y)
            path.down()
            path.begin_fill()
    
            for count in range(4):
                path.forward(20)
                path.left(90)
    
            path.end_fill()
    
    
        def offset(point):
            """Return offset of point in tiles."""
            x = (floor(point.x, 20) + 200) / 20
            y = (180 - floor(point.y, 20)) / 20
            index = int(x + y * 20)
            return index
    
    
        def valid(point):
            """Return True if point is valid in tiles."""
            index = offset(point)
    
            if tiles[index] == 0:
                return False
    
            index = offset(point + 19)
    
            if tiles[index] == 0:
                return False
    
            return point.x % 20 == 0 or point.y % 20 == 0
    
    
        def world():
            """Draw world using path."""
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
            """Move pacmasn and all ghosts."""
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
            """Change pacman aim if valid."""
            if valid(pacman + vector(x, y)):
                aim.x = x
                aim.y = y
        def change1(x1, y1):
            """Change pacman aim if valid."""
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

else:
    print('Not valid input for gamemode')
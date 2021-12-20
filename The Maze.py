import time
import turtle
import math
import winsound



#Sounds Effect
def play_sound():
    winsound.PlaySound("background.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)

def Lose_Sound():
    winsound.PlaySound("Lose.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)

def Win_Sound():
    winsound.PlaySound("win.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)

play_sound()

#The event listener


#Start Turtle
turtle.setup(1100, 780)
wnd = turtle.Screen()
wnd.bgcolor("gray")
wnd.title("THE MAZE")


#Set Shapes
turtle.register_shape('hamster.gif')
turtle.register_shape('swiz.gif')
turtle.register_shape('treasure.gif')
turtle.register_shape('lose.gif')
turtle.register_shape('win.gif')

running = False

def start_game():
    global running
    start_message.clear()
    running = True
    game_start()

def game_start():
    # Main Configures For Sounds
        named_tuple = time.localtime()
        fTime = named_tuple.tm_min
        stime = named_tuple.tm_sec
    # COINS SCORE
        Coins_Score = 0

        def Score():
            scorre = turtle.Turtle()
            scorre.penup()
            scorre.speed(0)
            scorre.color("gray", "red")
            scorre.goto((-490, 65))
            scorre.pendown()
            scorre.pensize(35)
            scorre.setx((-350))
            scorre.penup()
            scorre.goto(-490, 50)
            scorre.color("black", "red")
            scorre.pendown()
            scorre.write(arg="Score : " + str(Coins_Score), font=("Verdana", 18, "normal"))
            scorre.hideturtle()
            scorre.penup()

        Score()

        print("Developed by MaZeN G@D")

        # draw Maze Lines
        def drawMaze(s):
            Lines = turtle.Turtle()
            Lines.penup()
            Lines.setposition(s[0], s[1])
            Lines.speed(0)
            Lines.pendown()
            Lines.pensize(15)
            Lines.goto(s[2], s[3])
            Lines.hideturtle()

        d = (
            (-300, -300, 200, -300), (250, -300, 300, -300), (300, -300, 300, 300), (-200, 300, 300, 300),
            (-300, 300, -250, 300),
            (-300, -300, -300, 300), (-250, 240, -150, 240), (-100, 0, -100, 240), (-250, 180, -100, 180),
            (-250, -180, -250, 120),
            (-250, -180, 0, -180), (0, -180, 0, 0), (-100, 0, 0, 0), (-100, 60, 150, 60), (-50, 60, -50, 180),
            (0, 120, 0, 300),
            (-100, -60, 0, -60), (-100, -120, 0, -120), (-200, -120, -200, 180), (-150, -180, -150, 120),
            (-300, -240, -150, -240),
            (-100, -240, 200, -240), (50, -240, 50, -180), (50, -180, 300, -180), (0, -120, 50, -120),
            (125, -120, 125, 60),
            (100, -120, 150, -120), (200, -120, 250, -120), (225, -120, 225, 120), (0, 120, 225, 120),
            (200, 240, 200, 300),
            (200, 240, 250, 240), (50, 240, 150, 240), (150, 180, 150, 240), (50, 180, 250, 180))

        # Draw Maze Roads
        for i in d:
            drawMaze(i)

        # Coins positions
        Coinsp = {0: (75, -215), 1: (125, -215), 2: (-250, -210), 3: (-270, -265), 4: (-220, -150), 5: (-20, -150),
                  6: (-20, -30), 7: (-20, -90), 8: (-270, 150), 9: (-170, 150), 10: (-70, 180), 11: (-70, 120),
                  12: (-70, 30),
                  13: (-10, 30), 14: (-40, 30), 15: (240, 0), 16: (70, 210), 17: (100, 210), 18: (130, 210),
                  19: (220, 280),
                  20: (250, 280), 21: (280, 280), 22: (800, 800)}

        # Coins setup
        Coins = []
        for i in range(22):
            Coins.append(turtle.Turtle())
            Coins[i].penup()
            Coins[i].shape("treasure.gif")
            Coins[i].setposition(Coinsp[i][0], Coinsp[i][1])
            Coins[i].speed(0)

        # Monsters positions
        d2 = {0: (-280, -265, 280, -265, -150, -265), 1: (-280, -265, 280, -265, 50, -265),
              2: (20, -145, 280, -145, 20, -145),
              3: (20, -145, 280, -145, 230, -145), 4: (175, 205, 275, 205, 175, 205),
              5: (-280, 265, -20, 265, -270, 265),
              6: (-280, 265, -20, 265, -220, 265), 7: (-280, 265, -20, 265, -160, 265)}

        d3 = {0: (25, -100, 25, 40, 25, 30), 1: (25, -100, 25, 40, 25, -30), 2: (170, -100, 170, 100, 170, 60),
              3: (170, -100, 170, 100, 170, 0), 4: (250, -100, 250, 160, 250, 120), 5: (250, -100, 250, 160, 250, 0),
              6: (30, 140, 30, 280, 30, 180), 7: (-30, 80, -30, 280, -30, 240), 8: (-250, -220, -250, -180, -250, -220),
              9: (-130, -160, -130, 160, -130, 60), 10: (-130, -160, -130, 160, -130, -20),
              11: (100, -100, 100, 40, 100, 30),
              12: (100, -100, 100, 40, 100, -30)}

        # MonstersX
        Monster = []
        for i in range(8):
            Monster.append(turtle.Turtle())
            Monster[i].penup()
            Monster[i].shape("swiz.gif")
            Monster[i].setposition(d2[i][4], d2[i][5])
            Monster[i].speed(0)

        # Important For Second Repeat
        play_sound()

        # MonstersY
        Monster2 = []
        for i in range(13):
            Monster2.append(turtle.Turtle())
            Monster2[i].penup()
            Monster2[i].shape("swiz.gif")
            Monster2[i].setposition(d3[i][4], d3[i][5])
            Monster2[i].speed(0)

        # hamster (The Player)
        hamster = turtle.Turtle()
        hamster.penup()
        hamster.shape("hamster.gif")
        hamster.speed(0)
        hamster.setposition(230, -320)

        # keyboard input functions
        def up():
            for i in d:
                # Stil inside maze
                if hamster.xcor() in range(int(i[0]) - 15, int(i[2]) + 15) and hamster.ycor() in range(int(i[1]) - 20,
                                                                                                       int(i[3])):
                    return None

                # Outside maze
                elif hamster.xcor() in range(-250, -200) and hamster.ycor() > 300:
                    tr = turtle.Turtle()
                    wn = turtle.Screen()
                    tr.shape('win.gif')
                    Win_Sound()
                    time.sleep(1.5)
                    exit()
            return hamster.sety(hamster.ycor() + 10)

        #######################################Down#######################################
        def down():
            for i in d:
                # Stil inside maze
                if hamster.xcor() in range(int(i[0]) - 15, int(i[2]) + 15) and hamster.ycor() in range(int(i[1]) - 15,
                                                                                                       int(i[3]) + 23):
                    return None
                # Outside maze
                elif hamster.xcor() in range(-250, -200) and hamster.ycor() > 300:
                    tr = turtle.Turtle()
                    wn = turtle.Screen()
                    tr.shape('win.gif')
                    Win_Sound()
                    time.sleep(1.5)
                    exit()
            return hamster.sety(hamster.ycor() - 10)

        #######################################Left#######################################
        def left():
            for i in d:
                # Stil inside maze
                if hamster.xcor() in range(int(i[0]), int(i[2]) + 23) and hamster.ycor() in range(int(i[1]) - 15,
                                                                                                  int(i[3]) + 15):
                    return None

                # Outside maze
                elif hamster.xcor() in range(-250, -200) and hamster.ycor() > 300:
                    tr = turtle.Turtle()
                    wn = turtle.Screen()
                    tr.shape('win.gif')
                    Win_Sound()
                    time.sleep(1.5)
                    exit()
            return hamster.backward(10)

        #######################################Right#######################################
        def right():
            for i in d:
                # Stil inside maze
                if hamster.xcor() in range(int(i[0]) - 25, int(i[2])) and hamster.ycor() in range(int(i[1]) - 15,
                                                                                                  int(i[3]) + 15):
                    return None

                # Outside maze
                elif hamster.xcor() in range(-250, -200) and hamster.ycor() > 300:
                    tr = turtle.Turtle()
                    wn = turtle.Screen()
                    tr.shape('win.gif')
                    Win_Sound()
                    time.sleep(1.5)
                    exit()
            return hamster.forward(10)

        # keyboard inputs
        wnd.onkey(up, "Up")
        wnd.onkey(down, "Down")
        wnd.onkey(left, "Left")
        wnd.onkey(right, "Right")
        wnd.listen()

        Score()
        # Animate The Maze
        while True:

            for j in range(8):
                dist = math.sqrt(
                    math.pow(hamster.xcor() - Monster[j].xcor(), 2) + math.pow(hamster.ycor() - Monster[j].ycor(), 2))
                if (dist < 20):
                    tr = turtle.Turtle()
                    wn = turtle.Screen()
                    tr.shape('lose.gif')
                    Lose_Sound()
                    time.sleep(3.5)
                    exit()
                Monster[j].forward(6)
                if (Monster[j].xcor() < d2[j][0] or Monster[j].xcor() > d2[j][2] or Monster[j].ycor() < d2[j][1] or
                        Monster[j].ycor() > d2[j][
                            3]):
                    Monster[j].right(180)

            for q in range(13):
                dist2 = math.sqrt(
                    math.pow(hamster.xcor() - Monster2[q].xcor(), 2) + math.pow(hamster.ycor() - Monster2[q].ycor(), 2))
                if (dist2 < 20):
                    tr = turtle.Turtle()
                    wn = turtle.Screen()
                    tr.shape('lose.gif')
                    Lose_Sound()
                    time.sleep(3.5)
                    exit()
                Monster2[q].sety(Monster2[q].ycor() + 5)
                if (Monster2[q].xcor() < d3[q][0] or Monster2[q].xcor() > d3[q][2] or Monster2[q].ycor() < d3[q][1] or
                        Monster2[q].ycor() >
                        d3[q][3]):
                    Monster2[q].sety(Monster2[q].ycor() - (d3[q][3] - d3[q][1]))

            for g in range(22):
                dist3 = math.sqrt(
                    math.pow(hamster.xcor() - Coins[g].xcor(), 2) + math.pow(hamster.ycor() - Coins[g].ycor(), 2))

                # to Make Coins Looks Collected
                if (dist3 < 20):
                    Coins[g].hideturtle()
                    Coins[g].clear()
                    Coins[g].setposition(Coinsp[22][0], Coinsp[22][1])

                    Coins_Score += 1
                    Score()

            # To Make Sounds Too long
            if (((fTime) < (time.localtime().tm_min)) or (((stime + 7) % 64) < time.localtime().tm_sec)):
                play_sound()
                fTime = time.localtime().tm_min
                stime = time.localtime().tm_sec


screen = turtle.Screen()
screen.bgpic('back.gif')

start_message = turtle.Turtle()
start_message.hideturtle()
start_message.penup()
start_message.sety(-320)
start_message.write(" @@ Mazen Gad @@", align="center", font=("Courier", 14, "bold"))
start_message.penup()
start_message.sety(5)
start_message.write("Press SPACE to start", align="center", font=("Courier", 35, "bold"))
start_message.penup()

wnd.onkeypress(start_game, 'space')
wnd.listen()


wnd.mainloop()
import curses
from random import randint
#window setup
curses.initscr()
win = curses.newwin(20, 60, 0, 0) #y, x
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)
wall_smack = "you really cant drive"
#snake and food track
snake = [(4, 14), (4,13), (4, 12)] #tupel because then it cant be changed
food = (10,20)
win.addch(food[0], food[1], '&')
score = 0
#game logic

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0,2, 'Score ' + str(score) + " ")
    win.timeout(150 - (len(snake)) // 5 + len(snake)//10%120)


    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    #calculate next place for snake
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))

    #check if we hit wall
    if y == 0:
        print(wall_smack)
        break
    if y == 19:
        print(wall_smack)
        break
    if x == 0:
        print(wall_smack)
        break
    if x == 59:
        print(wall_smack)
        break

    #self collusion
    if snake[0] in snake [1:]: break

    #if food is eaten
    if snake == food:
        score += 1
        food = ()
        while food == ():
            food = (randint(1,18), randint(1,58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '&')
    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')



    # for c in snake:
    #     win.addch(c[0], c[1], '*')

    win.addch(snake[0][0], snake[0][1], '*')



curses.endwin()
print(score)

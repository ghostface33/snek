import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

#init curses
curses.initscr()
#no echo mode
curses.noecho()
#react to keypress
curses.cbreak()
#use arrow keys
stdscr = curses.newwin(20,60,0,0)
stdscr.keypad(1)
#no cursor
curses.curs_set(0)
#set title
stdscr.addstr(0,27,"SNAKE GAME")
#refresh
stdscr.refresh()
#create snake
snake = [[4,10], [4,9], [4,8]]
#create food
food = [10,20]
#add food to screen
stdscr.addch(food[0], food[1], '*')

#add snake to screen
stdscr.addch(snake[0][0], snake[0][1], '#')

key = KEY_RIGHT
#loop until gameover
while key !=  27:
    #get next key
    prevKey = key
    event = stdscr.getch()
    key = key if event == -1 else event

    #calculate next head
    if key == KEY_RIGHT:
        new_head = [snake[0][0], snake[0][1] + 1]
    elif key == KEY_LEFT:
        new_head = [snake[0][0], snake[0][1] - 1]
    elif key == KEY_UP:
        new_head = [snake[0][0] - 1, snake[0][1]]
    elif key == KEY_DOWN:
        new_head = [snake[0][0] + 1, snake[0][1]]

    #check for wall collision
    if (new_head[0] == 0 or new_head[0] == 19 or 
        new_head[1] == 0 or new_head[1] == 59):
        break

    #check for self collision
    if new_head in snake:
        break
    
    #add new head to snake
    snake.insert(0, new_head)
    
    #check if eat food
    if snake[0] == food:
        food = None
        while food is None:
            #calculate random food position
            nf = [
                randint(1, 18),
                randint(1, 58)
            ]
            food = nf if nf not in snake else None
        #add food to screen
        stdscr.addch(food[0], food[1], '*')
    else:    
        #remove tail from snake
        tail = snake.pop()
        #add tail to screen
        stdscr.addch(tail[0], tail[1], ' ')
    
    #add head to screen
    stdscr.addch(snake[0][0], snake[0][1], '#')

#gameover
curses.endwin()
print("\nGame Over")

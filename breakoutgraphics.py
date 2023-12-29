"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:


    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball_width = BALL_RADIUS
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, (window_width-ball_radius)/2, (window_height-ball_radius)/2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.click)
        onmousemoved(self.move)


        # Draw bricks
        self.brick_number = 0
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j < 2:
                    self.brick.fill_color = 'red'
                elif j < 4:
                    self.brick.fill_color = 'orange'
                elif j < 6:
                    self.brick.fill_color = 'yellow'
                elif j < 8:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=i*(brick_width+brick_spacing),
                                y=brick_offset+j*(brick_height+brick_spacing))

                self.brick_number += 1

        self.live = 3
        self.live_label = GLabel('Lives: ' + str(self.live))
        self.brick_label = GLabel('Bricks: ' + str(self.brick_number))
        self.window.add(self.live_label, x=5, y=20)
        self.window.add(self.brick_label, x=5, y=40)
        self.gameover = GLabel('GAMEOVER')
        self.gameover.font = '-50'
        self.gameover.color = 'red'
        self.youwin = GLabel('YOU WIN!')
        self.youwin.font = '-50'
        self.youwin.color = 'red'
    def move(self, mouse):
        if 0 <= mouse.x - self.paddle.width/2 <= self.window.width - self.paddle.width:
            self.paddle.x = mouse.x - self.paddle.width/2
        elif mouse.x - self.paddle.width/2 <= 0:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window.width - self.paddle.width



    def click(self, mouse):
        if self.__dy == 0:
            self.__dx = random.randint(-MAX_X_SPEED, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED




    def get_vx(self):
        return self.__dx


    def get_vy(self):
        return self.__dy

    def set_vx(self):
        self.__dx = -self.__dx

    def set_vy(self):
        self.__dy = -self.__dy

    def set_vx0(self):
        self.__dx = 0

    def set_vy0(self):
        self.__dy = 0





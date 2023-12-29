"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 20         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    live = NUM_LIVES
    brick_num = graphics.brick_number


    while True:
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        graphics.ball.move(vx, vy)
        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            graphics.set_vx()
        if graphics.ball.y <= 0:
            graphics.set_vy()
        if graphics.ball.y > graphics.window.height:
            graphics.window.remove(graphics.ball)
            graphics.window.add(graphics.ball, x=(graphics.window.width-graphics.ball_width)/2,
                                y=(graphics.window.height-graphics.ball_width)/2)
            graphics.set_vx0()
            graphics.set_vy0()
            live -= 1
            graphics.live_label.text = 'Lives: ' + str(live)
            if live == 0:
                graphics.window.add(graphics.gameover, x=90, y=graphics.window.height/2)
                graphics.window.remove(graphics.ball)
                break

        maybe_object1 = graphics.window.get_object_at(graphics.ball.x + graphics.ball_width/2, graphics.ball.y-1)
        maybe_object2 = graphics.window.get_object_at(1+graphics.ball.x + graphics.ball_width,
                                                      graphics.ball.y + graphics.ball_width/2)
        maybe_object3 = graphics.window.get_object_at(graphics.ball.x-1, graphics.ball.y + graphics.ball_width/2)
        maybe_object4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball_width/2,
                                                      1+graphics.ball.y + graphics.ball_width)
        if maybe_object1 is not None and maybe_object1 and maybe_object1 is not graphics.live_label and \
                maybe_object1 is not graphics.brick_label:
            if maybe_object1 is not graphics.paddle:
                graphics.window.remove(maybe_object1)
                brick_num -= 1
                graphics.brick_label.text = 'Bricks: ' + str(brick_num)
                graphics.set_vy()
            else:
                graphics.set_vy()

        elif maybe_object2 is not None and maybe_object2 is not graphics.live_label and \
                maybe_object2 is not graphics.brick_label:
            if maybe_object2 is not graphics.paddle:
                graphics.window.remove(maybe_object2)
                brick_num -= 1
                graphics.brick_label.text = 'Bricks: ' + str(brick_num)
                graphics.set_vx()
            else:
                graphics.set_vx()

        elif maybe_object3 is not None and maybe_object3 is not graphics.live_label and \
                maybe_object3 is not graphics.brick_label:
            if maybe_object3 is not graphics.paddle:
                graphics.window.remove(maybe_object3)
                brick_num -= 1
                graphics.brick_label.text = 'Bricks: ' + str(brick_num)
                graphics.set_vx()
            else:
                graphics.set_vx()

        elif maybe_object4 is not None and maybe_object4 is not graphics.live_label and \
                maybe_object4 is not graphics.brick_label:
            if maybe_object4 is not graphics.paddle:
                graphics.window.remove(maybe_object4)
                brick_num -= 1
                graphics.brick_label.text = 'Bricks: ' + str(brick_num)
                graphics.set_vy()
            else:
                graphics.set_vy()

        if brick_num == 0:
            graphics.window.add(graphics.youwin, x=90, y=graphics.window.height / 2)
            graphics.window.remove(graphics.ball)
            break


        pause(FRAME_RATE)
    # Add the animation loop here!


if __name__ == '__main__':
    main()

import pyglet
from vector import Vector
from ball import Ball
from math import atan2, cos, sin, sqrt

windowWidth = 900
windowHeight = 600
explosion_image = pyglet.image.load('exp.png')
explosions = []

window = pyglet.window.Window(windowWidth, windowHeight)
ball = Ball(64, Vector([300, 200]), windowWidth, windowHeight)
balls = [ball]


@window.event
def on_draw():
    window.clear()
    for b in balls:
        b.draw()

    for expl in explosions:
        expl.draw()


def updateBall(dt):
    for b in balls:
        b.move()


def dist(p1, p2):
    (x, y) = p1
    (z, w) = p2
    return sqrt((z - x)**2 + (w - y)**2)


def createExplosion(x, y):
    exp_animation = pyglet.image.ImageGrid(explosion_image, 4, 4).get_animation(1.0 / 30, False)
    exp_sprite = pyglet.sprite.Sprite(exp_animation)
    exp_sprite.x = x - exp_sprite.width / 2
    exp_sprite.y = y - exp_sprite.height / 2
    explosions.append(exp_sprite)

    @exp_sprite.event
    def on_animation_end():
        del(explosions[0])


@window.event
def on_mouse_press(x, y, button, modifiers):
    for b in balls:
        b.kick(x, y)

    createExplosion(x, y)


@window.event
def on_key_press(symbol, modifiers):
    balls.append(Ball(64, Vector([300, 200]), windowWidth, windowHeight))


pyglet.clock.schedule_interval(updateBall, 1.0 / 30)
pyglet.app.run()

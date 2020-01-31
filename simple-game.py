import pyglet
from math import atan2, cos, sin, sqrt

balls = []
ball_image = pyglet.image.load('ball.png')
framerate = 1.0 / 30

def newBall():
   global balls

   ball = pyglet.sprite.Sprite(ball_image, x=300, y=200)
   ball.xAcc, ball.yAcc = 0.0, -5.0
   ball.xVel, ball.yVel = 0.0, 0.0
   ball.image.anchor_x = ball.image.width // 2
   ball.image.anchor_y = ball.image.height // 2

   balls.append(ball)

newBall()

window = pyglet.window.Window(width=900, height=600)
@window.event
def on_key_press(symbol, modifiers):
   newBall()

@window.event
def on_draw():
   window.clear()
   for ball in balls:
      ball.draw()

def updateBall(dt):
   friction = 0.0

   for ball in balls:
      ball.xVel += ball.xAcc
      ball.yVel += ball.yAcc
      ball.x += ball.xVel
      ball.y += ball.yVel

      if ball.y - ball.image.anchor_y < 0:
         ball.y = ball.image.anchor_y
         ball.yVel = -ball.yVel + friction * ball.yVel

      if ball.y + (ball.height - ball.image.anchor_y) > window.height:
         ball.y = window.height - ball.image.anchor_y
         ball.yVel = -ball.yVel + friction * ball.yVel

      if ball.x - ball.image.anchor_x < 0:
         ball.x = ball.image.anchor_x
         ball.xVel = -ball.xVel + friction * ball.xVel

      if ball.x + (ball.width - ball.image.anchor_x) > window.width:
         ball.x = window.width - (ball.width - ball.image.anchor_x)
         ball.xVel = -ball.xVel + friction * ball.xVel

dist = lambda (x,y), (z,w): ((z-x)**2 + (w-y)**2)

@window.event
def on_mouse_press(x,y,button,modifiers):
   kick_speed = 60;
   for ball in balls:
      ballCenter = ball.x, ball.y

      if dist(ballCenter, (x,y)) < (ball.image.width/2) ** 2:
         forceAngle = atan2(ball.y - y, ball.x - x)
         ball.yVel = kick_speed * sin(forceAngle)
         ball.xVel = kick_speed * cos(forceAngle)

pyglet.clock.schedule_interval(updateBall, framerate)
pyglet.app.run()

